import asyncio
import json
import logging
import os
import re
import subprocess
import time
import uuid

from avocado.core.dependencies.requirements import cache
from avocado.core.plugin_interfaces import CLI, DeploymentSpawner, Init
from avocado.core.resolver import ReferenceResolutionAssetType
from avocado.core.settings import settings
from avocado.core.spawners.common import SpawnCapabilities, SpawnerMixin, SpawnMethod
from avocado.core.teststatus import STATUSES_NOT_OK
from avocado.core.version import VERSION
from avocado.utils import distro
from avocado.utils.asset import Asset
from avocado.utils.podman import AsyncPodman, PodmanException

LOG = logging.getLogger(__name__)


class PodmanSpawnerException(PodmanException):
    """Errors more closely related to the spawner functionality"""


class PodmanSpawnerInit(Init):

    description = "Podman (container) based spawner initialization"

    def initialize(self):
        section = "spawner.podman"

        help_msg = "Path to the podman binary"
        settings.register_option(
            section=section, key="bin", help_msg=help_msg, default="/usr/bin/podman"
        )

        this_distro = distro.detect()
        if this_distro != distro.UNKNOWN_DISTRO:
            default_distro = f"{this_distro.name}:{this_distro.version}"
        else:
            default_distro = "fedora:latest"
        help_msg = (
            f"Image name to use when creating the container. "
            f"The first default choice is a container image "
            f"matching the current OS. If unable to detect, "
            f"default becomes the latest Fedora release. Default "
            f"on this system: {default_distro}"
        )
        settings.register_option(
            section=section, key="image", help_msg=help_msg, default=default_distro
        )

        help_msg = (
            "Avocado egg path to be used during initial bootstrap "
            "of avocado inside the isolated environment. By default, "
            "Avocado will try to download (or get from cache) an "
            "egg from its repository. Please use a valid URL, including "
            'the protocol (for local files, use the "file:///" prefix).'
        )

        settings.register_option(
            section=section, key="avocado_spawner_egg", help_msg=help_msg, default=None
        )

        help_msg = (
            "Prefix to use when tagging images that are created by the "
            "Podman spawner."
        )

        settings.register_option(
            section=section,
            key="image_tag_prefix",
            help_msg=help_msg,
            default="avocado_generated",
        )


class PodmanCLI(CLI):

    name = "podman"
    description = 'podman spawner command line options for "run"'

    def configure(self, parser):
        super().configure(parser)
        parser = parser.subcommands.choices.get("run", None)
        if parser is None:
            return

        parser = parser.add_argument_group("podman spawner specific options")
        settings.add_argparser_to_option(
            namespace="spawner.podman.bin",
            parser=parser,
            long_arg="--spawner-podman-bin",
            metavar="PODMAN_BIN",
        )

        settings.add_argparser_to_option(
            namespace="spawner.podman.image",
            parser=parser,
            long_arg="--spawner-podman-image",
            metavar="CONTAINER_IMAGE",
        )

        namespace = "spawner.podman.avocado_spawner_egg"
        long_arg = "--spawner-podman-avocado-egg"
        settings.add_argparser_to_option(
            namespace=namespace, parser=parser, long_arg=long_arg, metavar="AVOCADO_EGG"
        )

    def run(self, config):
        pass


class PodmanSpawner(DeploymentSpawner, SpawnerMixin):

    description = "Podman (container) based spawner"
    METHODS = [SpawnMethod.STANDALONE_EXECUTABLE]
    CAPABILITIES = [
        SpawnCapabilities.AUTOMATIC_ENVIRONMENT_PROVISIONING,
        SpawnCapabilities.AVOCADO_DEPLOYMENT,
        SpawnCapabilities.ENVIRONMENT_PRESERVATION,
        SpawnCapabilities.FILESYSTEM_SHARING,
    ]

    _PYTHON_VERSIONS_CACHE = {}

    def __init__(self, config=None, job=None):  # pylint: disable=W0231
        SpawnerMixin.__init__(self, config, job)
        self.environment = f"podman:{self.config.get('spawner.podman.image')}"
        self._podman_version = (None, None, None)
        self._podman = None

    def _get_podman_version(self):
        podman_bin = self.config.get("spawner.podman.bin")
        try:
            cmd = [podman_bin, "--version"]
            process = subprocess.Popen(
                cmd,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
            )
            out, _ = process.communicate()
        except subprocess.SubprocessError as ex:
            raise PodmanException("Failed to get podman version information") from ex

        match = re.match(rb"podman version (\d+)\.(\d+).(\d+)\n", out)
        if match:
            major, minor, release = match.groups()
            return (int(major), int(minor), int(release))
        raise PodmanException(
            f"Failed to get podman version information: "
            f'output received "{out}" does not match expected output'
        )

    def is_operational(self):
        try:
            _ = self.podman_version
        except PodmanException as ex:
            LOG.error(ex)
            return False

        if self.podman_version[0] >= 3:
            return True
        LOG.error(
            f"The podman binary f{self.podman_bin} did not report a suitable version (>= 3.0)"
        )
        return False

    @property
    def podman_version(self):
        if self._podman_version == (None, None, None):
            self._podman_version = self._get_podman_version()
        return self._podman_version

    @property
    def podman(self):
        if self._podman is None:
            podman_bin = self.config.get("spawner.podman.bin")
            try:
                self._podman = AsyncPodman(podman_bin)
            except PodmanException as ex:
                LOG.error(ex)
        return self._podman

    def _get_podman_state(self, runtime_task):
        if runtime_task.spawner_handle is None:
            return False
        podman_bin = self.config.get("spawner.podman.bin")
        cmd = [
            podman_bin,
            "ps",
            "--all",
            "--format={{.State}}",
            f"--filter=id={runtime_task.spawner_handle}",
        ]
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        out, _ = process.communicate()
        return out

    def is_task_alive(self, runtime_task):  # pylint: disable=W0221
        out = self._get_podman_state(runtime_task)
        if self.podman_version[0] < 4:
            return out.startswith(b"Up ")

        if out == b"running\n":
            return True
        if out == b"created\n":
            # give the container a chance to transition to running
            time.sleep(0.1)
            out = self._get_podman_state(runtime_task)
            return out == b"running\n"
        return False

    def _fetch_asset(self, url):
        cachedirs = self.config.get("datadir.paths.cache_dirs")
        asset = Asset(url, cache_dirs=cachedirs)
        return asset.fetch()

    def get_eggs_paths(self, py_major, py_minor):
        """Return the basic eggs needed to bootstrap Avocado.

        This will return a tuple with the current location and where this
        should be deployed.
        """
        result = []
        # Setuptools
        # For now let's pin to setuptools 59.2.
        # TODO: Automatically get latest setuptools version.
        eggs = [
            f"https://github.com/avocado-framework/setuptools/releases/download/v59.2.0/setuptools-59.2.0-py{py_major}.{py_minor}.egg"
        ]
        local_egg = self.config.get("spawner.podman.avocado_spawner_egg")
        if local_egg:
            eggs.append(local_egg)
        else:
            remote_egg = f"https://github.com/avocado-framework/avocado/releases/download/{VERSION}/avocado_framework-{VERSION}-py{py_major}.{py_minor}.egg"
            eggs.append(remote_egg)

        for url in eggs:
            path = self._fetch_asset(url)
            to = os.path.join("/tmp/", os.path.basename(path))
            result.append((path, to))
        return result

    @property
    async def python_version(self):
        image = self.config.get("spawner.podman.image")
        if image not in self._PYTHON_VERSIONS_CACHE:
            if not self.podman:
                msg = "Cannot get Python version: self.podman not defined."
                LOG.debug(msg)
                return None, None, None
            result = await self.podman.get_python_version(image)
            self._PYTHON_VERSIONS_CACHE[image] = result
        return self._PYTHON_VERSIONS_CACHE[image]

    async def deploy_artifacts(self):
        pass

    async def deploy_avocado(self, where):
        # Deploy all the eggs to container inside /tmp/
        major, minor, _ = await self.python_version
        eggs = self.get_eggs_paths(major, minor)

        for egg, to in eggs:
            await self.podman.copy_to_container(where, egg, to)

    async def _create_container_for_task(
        self, runtime_task, env_args, test_output=None
    ):
        mount_status_server_socket = False
        mounted_status_server_socket = "/tmp/.status_server.sock"
        status_server_uri = runtime_task.task.status_services[0].uri
        if ":" not in status_server_uri:
            # a unix domain socket is being used
            mount_status_server_socket = True
            runtime_task.task.status_services[0].uri = mounted_status_server_socket

        _, _, python_binary = await self.python_version
        full_module_name = (
            runtime_task.task.runnable.pick_runner_module_from_entry_point_kind(
                runtime_task.task.runnable.kind
            )
        )
        if full_module_name is None:
            msg = f"Could not determine Python module name for runnable with kind {runtime_task.task.runnable.kind}"
            raise PodmanSpawnerException(msg)

        entry_point_args = [python_binary, "-m", full_module_name, "task-run"]

        test_opts = []
        if runtime_task.task.category == "test" and runtime_task.task.runnable.assets:
            for asset_type, asset in runtime_task.task.runnable.assets:
                if asset_type in (
                    ReferenceResolutionAssetType.TEST_FILE,
                    ReferenceResolutionAssetType.DATA_FILE,
                ):
                    if os.path.exists(asset):
                        to = os.path.join("/tmp", asset)
                        test_opts.append("-v")
                        test_opts.append(f"{os.path.abspath(asset)}:{to}:ro")
                if asset_type == ReferenceResolutionAssetType.TEST_FILE:
                    # The URI may contain a test specification within the file,
                    # which is separated by a colon
                    if runtime_task.task.runnable.uri.split(":")[0] == asset:
                        runtime_task.task.runnable.uri = os.path.join(
                            "/tmp", runtime_task.task.runnable.uri
                        )

        task = runtime_task.task
        entry_point_args.extend(task.get_command_args())
        entry_point = json.dumps(entry_point_args)
        entry_point_arg = "--entrypoint=" + entry_point

        if mount_status_server_socket:
            status_server_opts = (
                "--privileged",
                "-v",
                f"{status_server_uri}:{mounted_status_server_socket}",
            )
        else:
            status_server_opts = ("--net=host",)

        output_opts = ()
        if test_output:
            output_opts = (
                "-v",
                f"{test_output}:{runtime_task.task.runnable.output_dir}",
            )

        image, _ = self._get_image_from_cache(runtime_task)
        if not image:
            image = self.config.get("spawner.podman.image")

        envs = [f"-e={k}={v}" for k, v in env_args.items()]
        # pylint: disable=W0201
        _, stdout, _ = await self.podman.execute(
            "create",
            *status_server_opts,
            *output_opts,
            *test_opts,
            entry_point_arg,
            *envs,
            image,
        )
        return stdout.decode().strip()

    async def spawn_task(self, runtime_task):
        self.create_task_output_dir(runtime_task)

        major, minor, _ = await self.python_version
        # Return only the "to" location
        eggs = self.get_eggs_paths(major, minor)
        destination_eggs = ":".join(map(lambda egg: str(egg[1]), eggs))
        env_args = {"PYTHONPATH": destination_eggs}
        output_dir_path = self.task_output_dir(runtime_task)
        try:
            container_id = await self._create_container_for_task(
                runtime_task, env_args, output_dir_path
            )
        except PodmanException as ex:
            LOG.error("Could not create podman container: %s", ex)
            return False

        runtime_task.spawner_handle = container_id

        await self.deploy_avocado(container_id)

        try:
            # pylint: disable=W0201
            returncode, _, _ = await self.podman.start(container_id)
        except PodmanException as ex:
            LOG.error("Could not start container: %s", ex)
            return False

        return returncode == 0

    def create_task_output_dir(self, runtime_task):
        output_dir_path = self.task_output_dir(runtime_task)
        output_podman_path = "/tmp/.avocado_task_output_dir"

        os.makedirs(output_dir_path, exist_ok=True)
        runtime_task.task.setup_output_dir(output_podman_path)

    async def wait_task(self, runtime_task):
        while True:
            if not self.is_task_alive(runtime_task):
                return
            await asyncio.sleep(0.1)

    async def terminate_task(self, runtime_task):
        try:
            await self.podman.execute(
                "kill", "--signal=TERM", runtime_task.spawner_handle
            )
        except PodmanException as ex:
            LOG.error("Could not signal termination to task on container: %s", ex)
            return False
        soft_interval = self.config.get(
            "runner.task.interval.from_soft_to_hard_termination"
        )
        await asyncio.sleep(soft_interval)
        try:
            await self.podman.stop(runtime_task.spawner_handle)
        except PodmanException as ex:
            LOG.error("Could not stop container: %s", ex)
            return False
        hard_interval = self.config.get(
            "runner.task.interval.from_hard_termination_to_verification"
        )
        await asyncio.sleep(hard_interval)
        info = await self.podman.get_container_info(runtime_task.spawner_handle)
        return info.get("Exited", False)

    @staticmethod
    async def check_task_requirements(runtime_task):
        """Check the runtime task requirements needed to be able to run"""
        # right now, limit the check to the runner availability.
        if runtime_task.task.runnable.runner_command() is None:
            return False
        return True

    async def _create_and_tag_image(self, runtime_task):
        _, stdout, _ = await self.podman.execute(
            "commit", "-q", runtime_task.spawner_handle
        )
        image_id = stdout.decode().strip()
        tag_prefix = self.config.get("spawner.podman.image_tag_prefix")
        base_image = self.config.get("spawner.podman.image")
        kind = runtime_task.task.runnable.kind
        name = runtime_task.task.runnable.kwargs.get("name")
        tag = f"{tag_prefix}_{base_image}_{kind}_{name}".replace(":", "_")
        try:
            _, _, _ = await self.podman.execute("tag", image_id, tag)
        except PodmanException as ex:
            LOG.warning("Could not tag image %s with %s: %s", image_id, tag, ex)
        return image_id

    async def update_requirement_cache(
        self, runtime_task, result
    ):  # pylint: disable=W0221
        environment_id, _ = self._get_image_from_cache(runtime_task, True)
        if result in STATUSES_NOT_OK:
            cache.delete_environment(self.environment, environment_id)
            return
        image_id = await self._create_and_tag_image(runtime_task)
        cache.update_environment(self.environment, environment_id, image_id)
        cache.update_requirement_status(
            self.environment,
            image_id,
            runtime_task.task.runnable.kind,
            runtime_task.task.runnable.kwargs.get("name"),
            True,
        )

    async def save_requirement_in_cache(self, runtime_task):  # pylint: disable=W0221
        image_id = str(uuid.uuid4())
        _, requirements = self._get_image_from_cache(runtime_task)
        if requirements:
            for requirement_type, requirement in requirements:
                cache.set_requirement(
                    self.environment, image_id, requirement_type, requirement
                )
        cache.set_requirement(
            self.environment,
            image_id,
            runtime_task.task.runnable.kind,
            runtime_task.task.runnable.kwargs.get("name"),
            False,
        )

    async def is_requirement_in_cache(self, runtime_task):  # pylint: disable=W0221
        environment, _ = self._get_image_from_cache(runtime_task, use_task=True)
        if not environment:
            return False
        if cache.is_environment_prepared(environment):
            return True
        return None

    def _get_image_from_cache(self, runtime_task, use_task=False):
        def _get_all_finished_requirements(requirement_tasks):
            all_finished_requirements = []
            for requirement in requirement_tasks:
                all_finished_requirements.extend(
                    _get_all_finished_requirements(requirement.dependencies)
                )
                runnable = requirement.task.runnable
                all_finished_requirements.append(
                    (runnable.kind, runnable.kwargs.get("name"))
                )
            return all_finished_requirements

        finished_requirements = []
        if use_task:
            finished_requirements.append(
                (
                    runtime_task.task.runnable.kind,
                    runtime_task.task.runnable.kwargs.get("name"),
                )
            )
        finished_requirements.extend(
            _get_all_finished_requirements(runtime_task.dependencies)
        )
        if not finished_requirements:
            return None, None

        runtime_task_kind, runtime_task_name = finished_requirements[0]
        cache_entries = cache.get_all_environments_with_requirement(
            self.environment, runtime_task_kind, runtime_task_name
        )
        if not cache_entries:
            return None, None
        for image, requirements in cache_entries.items():
            if len(finished_requirements) == len(requirements):
                if set(requirements) == set(finished_requirements):
                    return image, requirements
        return None, None

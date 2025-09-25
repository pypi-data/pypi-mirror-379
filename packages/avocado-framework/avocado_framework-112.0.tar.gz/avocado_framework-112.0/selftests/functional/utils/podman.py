from avocado import Test
from avocado.utils.podman import AsyncPodman, Podman


class PodmanTest(Test):
    def test_python_version(self):
        """
        :avocado: dependency={"type": "package", "name": "podman", "action": "check"}
        :avocado: dependency={"type": "podman-image", "uri": "fedora:40"}
        :avocado: tags=slow
        """
        podman = Podman()
        result = podman.get_python_version("fedora:40")
        self.assertEqual(result, (3, 12, "/usr/bin/python3"))

    def test_container_info(self):
        """
        :avocado: dependency={"type": "package", "name": "podman", "action": "check"}
        :avocado: dependency={"type": "podman-image", "uri": "fedora:40"}
        :avocado: tags=slow
        """
        podman = Podman()
        _, stdout, _ = podman.execute("create", "fedora:40", "/bin/bash")
        container_id = stdout.decode().strip()
        result = podman.get_container_info(container_id)
        self.assertEqual(result["Id"], container_id)

        podman.execute("rm", container_id)

        result = podman.get_container_info(container_id)
        self.assertEqual(result, {})


class AsyncPodmanTest(Test):
    async def test_python_version(self):
        """
        :avocado: dependency={"type": "package", "name": "podman", "action": "check"}
        :avocado: dependency={"type": "podman-image", "uri": "fedora:40"}
        :avocado: tags=slow
        """
        podman = AsyncPodman()
        result = await podman.get_python_version("fedora:40")
        self.assertEqual(result, (3, 12, "/usr/bin/python3"))

    async def test_container_info(self):
        """
        :avocado: dependency={"type": "package", "name": "podman", "action": "check"}
        :avocado: dependency={"type": "podman-image", "uri": "fedora:40"}
        :avocado: tags=slow
        """
        podman = AsyncPodman()
        _, stdout, _ = await podman.execute("create", "fedora:40", "/bin/bash")
        container_id = stdout.decode().strip()
        result = await podman.get_container_info(container_id)
        self.assertEqual(result["Id"], container_id)

        await podman.execute("rm", container_id)

        result = await podman.get_container_info(container_id)
        self.assertEqual(result, {})

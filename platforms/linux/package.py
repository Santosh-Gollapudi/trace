import subprocess

from interfaces.package import PackageInterface


class LinuxPackage(PackageInterface):

    def install(self, package):
        result = subprocess.run(
            ["sudo", "apt", "install", "-y", package],
            capture_output=True,
            text=True
        )

        return result.returncode == 0

    def remove(self, package):
        result = subprocess.run(
            ["sudo", "apt", "remove", "-y", package],
            capture_output=True,
            text=True
        )

        return result.returncode == 0
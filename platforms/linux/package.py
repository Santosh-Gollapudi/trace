import subprocess

from interfaces.package import PackageInterface


class LinuxPackage(PackageInterface):

    def install(self, package):
        result = subprocess.run(
            ["sudo", "apt", "install", "-y", package],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        if result.returncode == 0:
            status = "installed"
        elif "unable to locate package" in error.lower():
            status = "not_found"
        else:
            status = "failed"

        return {
            "status": status,
            "output": output,
            "error": error,
            "returncode": result.returncode
        }

    def remove(self, package):
        result = subprocess.run(
            ["sudo", "apt", "remove", "-y", package],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        if result.returncode == 0:
            status = "removed"
        elif "unable to locate package" in error.lower():
            status = "not_found"
        else:
            status = "failed"

        return {
            "status": status,
            "output": output,
            "error": error,
            "returncode": result.returncode
        }
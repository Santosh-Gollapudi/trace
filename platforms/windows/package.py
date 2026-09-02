import subprocess

from interfaces.package import PackageInterface


class WindowsPackage(PackageInterface):

    def install(self, package):
        result = subprocess.run(
            ["winget", "install", "--id", package, "--exact"],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        if result.returncode == 0:
            status = "installed"
        elif "already installed" in output.lower() and "no available upgrade" in output.lower():
            status = "already_installed"
        elif "no package found" in output.lower():
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
            ["winget", "uninstall", "--id", package, "--exact"],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        if result.returncode == 0:
            status = "removed"
        elif "no installed package found" in output.lower():
            status = "not_found"
        else:
            status = "failed"

        return {
            "status": status,
            "output": output,
            "error": error,
            "returncode": result.returncode
        }
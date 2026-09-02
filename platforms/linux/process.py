import subprocess

from interfaces.process import ProcessInterface


class LinuxProcess(ProcessInterface):

    def list_processes(self):
        result = subprocess.run(
            ["ps", "-e"],
            capture_output=True,
            text=True
        )

        return result.stdout

    def kill(self, pid):
        result = subprocess.run(
            ["kill", str(pid)],
            capture_output=True,
            text=True
        )

        return result.returncode == 0
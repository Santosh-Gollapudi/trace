import subprocess

from interfaces.process import ProcessInterface


class WindowsProcess(ProcessInterface):

    def list_processes(self):
        result = subprocess.run(
            ["tasklist"],
            capture_output=True,
            text=True
        )

        return result.stdout

    def kill(self, pid):
        result = subprocess.run(
            ["taskkill", "/PID", str(pid), "/F"],
            capture_output=True,
            text=True
        )

        return result.returncode == 0
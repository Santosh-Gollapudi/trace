import subprocess

from interfaces.power import PowerInterface


class WindowsPower(PowerInterface):

    def battery(self):
        result = subprocess.run(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_Battery).EstimatedChargeRemaining"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return "Unable to read battery status."

        value = result.stdout.strip()

        if not value:
            return "No battery detected."

        return f"{value}%"

    def shutdown(self):
        result = subprocess.run(
            ["shutdown", "/s", "/t", "0"],
            capture_output=True,
            text=True
        )

        return result.returncode == 0
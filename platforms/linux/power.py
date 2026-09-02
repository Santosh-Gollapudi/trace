from pathlib import Path
import subprocess

from interfaces.power import PowerInterface


class LinuxPower(PowerInterface):

    def battery(self):
        batteries = list(Path("/sys/class/power_supply").glob("BAT*/capacity"))

        if not batteries:
            return "No battery detected."

        try:
            value = batteries[0].read_text().strip()
            return f"{value}%"
        except OSError:
            return "Unable to read battery status."

    def shutdown(self):
        result = subprocess.run(
            ["systemctl", "poweroff"],
            capture_output=True,
            text=True
        )

        return result.returncode == 0
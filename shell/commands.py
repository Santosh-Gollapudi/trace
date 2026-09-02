from shell.command import BaseCommand


class HelpCommand(BaseCommand):

    def __init__(self, registry):
        self.registry = registry

    def execute(self, command):
        print("\nAvailable commands:\n")

        for name in sorted(self.registry.commands):
            print(f"  {name}")

        print()

class VersionCommand(BaseCommand):

    def __init__(self, core):
        self.core = core

    def execute(self, command):
        print(self.core.config.get("app", "version"))

class StatusCommand(BaseCommand):

    def execute(self, command):
        print("READY")

class ExitCommand(BaseCommand):

    def execute(self, command):
        raise SystemExit

class PluginsCommand(BaseCommand):

    def __init__(self, core):
        self.core = core

    def execute(self, command):
        plugins = self.core.services.plugins.list_plugins()

        print("\nLoaded Plugins:\n")

        for plugin in plugins:
            print(f"- {plugin.name} v{plugin.version}")

class PwdCommand(BaseCommand):

    def __init__(self, system_service):
        self.system = system_service

    def execute(self, command):
        print(self.system.pwd())

class CdCommand(BaseCommand):

    def __init__(self, system_service):
        self.system = system_service

    def execute(self, command):

        if not command.args:
            print("Usage: cd <directory>")
            return

        if not self.system.cd(command.args[0]):
            print("Directory not found.")

class LsCommand(BaseCommand):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def execute(self, command):
        for item in self.filesystem.list_directory("."):
            print(item.name)

class ExistsCommand(BaseCommand):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def execute(self, command):

        if not command.args:
            print("Usage: exists <file>")
            return

        print(self.filesystem.exists(command.args[0]))

class MkdirCommand(BaseCommand):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def execute(self, command):

        if not command.args:
            print("Usage: mkdir <directory>")
            return

        self.filesystem.mkdir(command.args[0])

class TouchCommand(BaseCommand):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def execute(self, command):

        if not command.args:
            print("Usage: touch <file>")
            return

        self.filesystem.touch(command.args[0])

class CatCommand(BaseCommand):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def execute(self, command):

        if not command.args:
            print("Usage: cat <file>")
            return

        text = self.filesystem.read(command.args[0])

        if text is None:
            print("File not found.")
            return

        print(text)

class WriteCommand(BaseCommand):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def execute(self, command):

        if len(command.args) < 2:
            print("Usage: write <file> <text>")
            return

        filename = command.args[0]
        text = " ".join(command.args[1:])

        self.filesystem.write(filename, text)

        print("File written successfully.")

class AppendCommand(BaseCommand):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def execute(self, command):

        if len(command.args) < 2:
            print("Usage: append <file> <text>")
            return

        filename = command.args[0]
        text = " ".join(command.args[1:])

        self.filesystem.append(filename, text)

        print("Text appended.")
        
class IpCommand(BaseCommand):
    name = "ip"
    description = "Show the current IP address"
    
    def __init__(self, network_service):
        self.network = network_service

    def execute(self, args):
        print(self.network.current_ip())
        
class WifiCommand(BaseCommand):
    name = "wifi"
    description = "Scan for available Wi-Fi networks"
    
    def __init__(self, network_service):
        self.network = network_service

    def execute(self, args):
        networks = self.network.scan_wifi()
        if not networks:
            print("No Wi-Fi networks found.")
        else:
            print("Available Wi-Fi networks:")
            for network in networks:
                print(f"- {network}")
                
class ProcessesCommand(BaseCommand):
    name = "ps"
    description = "List running processes"

    def __init__(self, process_service):
        self.process = process_service

    def execute(self, args):
        output = self.process.list_processes()
        print(output)
        
class BatteryCommand(BaseCommand):
    name = "battery"
    description = "Show battery status"

    def __init__(self, power_service):
        self.power = power_service

    def execute(self, args):
        print(self.power.battery())

class PackageCommand(BaseCommand):

    name = "package"
    description = "Manage system packages"

    def __init__(self, package_service):
        self.package = package_service

    def execute(self, command):
        if len(command.args) < 2:
            print("Usage: package <install|remove> <package>")
            return

        action = command.args[0].lower()
        package = command.args[1]

        if action == "install":
            print(f'Install "{package}"? [y/N]: ', end="")
            confirmation = input().strip().lower()

            if confirmation != "y":
                print("Cancelled.")
                return

            result = self.package.install(package)

            if result["status"] == "installed":
                print("Package installed successfully.")

            elif result["status"] == "already_installed":
                print("Package is already installed and no update is available.")

            elif result["status"] == "not_found":
                print("Package not found.")

            else:
                print("Package installation failed.")

            if result["output"]:
                print(result["output"])
            if result["error"]:
                print(result["error"])

        elif action == "remove":
            print(f'Remove "{package}"? [y/N]: ', end="")
            confirmation = input().strip().lower()

            if confirmation != "y":
                print("Cancelled.")
                return

            result = self.package.remove(package)

            if result["status"] == "removed":
                print("Package removed successfully.")

            elif result["status"] == "not_found":
                print("Package is not installed.")

            else:
                print("Package removal failed.")

            if result["output"]:
                print(result["output"])
            if result["error"]:
                print(result["error"])

        else:
            print("Usage: package <install|remove> <package>")
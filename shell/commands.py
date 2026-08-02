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
        
class LsCommand(BaseCommand):

    def __init__(self, system_service):
        self.system = system_service

    def execute(self, command):
        for item in self.system.ls():
            print(item.name)

class ExistsCommand(BaseCommand):

    def __init__(self, system_service):
        self.system = system_service

    def execute(self, command):

        if not command.args:
            print("Usage: exists <file>")
            return

        print(self.system.exists(command.args[0]))
        
class CdCommand(BaseCommand):

    def __init__(self, system_service):
        self.system = system_service

    def execute(self, command):

        if not command.args:
            print("Usage: cd <directory>")
            return

        if not self.system.cd(command.args[0]):
            print("Directory not found.")
            
    
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
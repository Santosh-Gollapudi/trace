from shell.registry import CommandRegistry
from shell.parser import parse
from shell.commands import (
    HelpCommand,
    VersionCommand,
    StatusCommand,
    PluginsCommand,
    PwdCommand,
    LsCommand,
    ExistsCommand,
    CdCommand,
)

class Shell:

    def __init__(self, core):

        self.registry = CommandRegistry()

        self.registry.register(
            "help",
            HelpCommand(self.registry)
        )

        self.registry.register(
            "version",
            VersionCommand(core)
        )

        self.registry.register(
            "status",
            StatusCommand()
        )
        
        self.registry.register(
            "plugins",
            PluginsCommand(core)
        )

        for plugin in core.plugins.get_plugins():
            plugin.register_commands(self.registry)
        self.registry.register(
            "pwd",
            PwdCommand(core.services.system)
        )

        self.registry.register(
            "ls",
            LsCommand(core.services.system)
        )

        self.registry.register(
            "exists",
            ExistsCommand(core.services.system)
        )

        self.registry.register(
            "cd",
            CdCommand(core.services.system)
        )

    def run(self):

        while True:
            command = parse(input("jarvis> "))
            self.registry.execute(command)
            
    
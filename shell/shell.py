from shell.registry import CommandRegistry
from shell.parser import parse
from shell.commands import (
    AppendCommand,
    ExitCommand,
    HelpCommand,
    MkdirCommand,
    VersionCommand,
    StatusCommand,
    PluginsCommand,
    PwdCommand,
    LsCommand,
    ExistsCommand,
    CdCommand,
    TouchCommand,
    CatCommand,
    WriteCommand,    
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
            "cd",
            CdCommand(core.services.system)
        )
        self.registry.register(
            "ls",
            LsCommand(core.services.filesystem)
        )

        self.registry.register(
            "exists",
            ExistsCommand(core.services.filesystem)
        )

        self.registry.register(
            "mkdir",
            MkdirCommand(core.services.filesystem)
        )

        self.registry.register(
            "touch",
            TouchCommand(core.services.filesystem)
        )

        self.registry.register(
            "cat",
            CatCommand(core.services.filesystem)
        )
      
        self.registry.register(
            "exit",
            ExitCommand()
        )
        self.registry.register(
            "write",
            WriteCommand(core.services.filesystem)
        )
        self.registry.register(
            "append",
            AppendCommand(core.services.filesystem)
)

    def run(self):

        while True:
            command = parse(input("trace> "))
            self.registry.execute(command)
            

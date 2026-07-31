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

    def run(self):

        while True:

            command = parse(input("jarvis> "))

            self.registry.execute(command)
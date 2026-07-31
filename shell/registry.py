class CommandRegistry:

    def __init__(self):
        self.commands = {}

    def register(self, name, command):
        self.commands[name] = command

    def execute(self, command):

        if command.name not in self.commands:
            print(f"Unknown command: {command.name}")
            return

        self.commands[command.name].execute(command)
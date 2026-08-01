from shell.command import BaseCommand


class HelloCommand(BaseCommand):

    def execute(self, command):
        print("Hello from Example Plugin!")
        

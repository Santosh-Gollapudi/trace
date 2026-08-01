from core.plugin import Plugin
from plugins.example.commands import HelloCommand


class ExamplePlugin(Plugin):

    @property
    def name(self):
        return "Example Plugin"

    @property
    def version(self):
        return "1.0"

    def register(self):
        print("✓ Example Plugin v1.0 loaded")

    def register_commands(self, registry):
        registry.register(
            "hello",
            HelloCommand()
        )
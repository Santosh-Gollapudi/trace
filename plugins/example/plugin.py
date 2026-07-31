from core.plugin import Plugin


class ExamplePlugin(Plugin):

    @property
    def name(self):
        return "Example Plugin"

    @property
    def version(self):
        return "1.0"

    def register(self):
        print(f"✓ {self.name} v{self.version} loaded")
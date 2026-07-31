"""
JARVIS AI Assistant
-------------------
Plugin manager.
"""

import importlib
from pathlib import Path


class PluginManager:

    def __init__(self):
        self.plugins = []

    def load_plugins(self):

        plugin_root = Path("plugins")

        for folder in plugin_root.iterdir():

            if not folder.is_dir():
                continue

            plugin_file = folder / "plugin.py"

            if plugin_file.exists():

                module_name = f"plugins.{folder.name}.plugin"

                module = importlib.import_module(module_name)

                plugin_class = getattr(module, "ExamplePlugin", None)

                if plugin_class:

                    plugin = plugin_class()

                    plugin.register()

                    self.plugins.append(plugin)

    def list_plugins(self):

        return self.plugins
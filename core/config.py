"""
TRACE AI Assistant
-------------------
Configuration loader.
"""

from pathlib import Path
import yaml


class ConfigManager:
    """Loads application configuration."""

    def __init__(self):
        self.config = {}

    def load(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        config_path = BASE_DIR / "config" / "version.yaml"

        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as file:
                self.config = yaml.safe_load(file)

        return self.config

    def get(self, *keys):
        value = self.config
        for key in keys:
            value = value[key]
        return value
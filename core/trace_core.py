"""
TRACE AI Assistant
-------------------
Main application core.
"""

from core.logger import logger
from core.config import ConfigManager
from core.plugin_manager import PluginManager
from core.event_bus import EventBus
from core.services import ServiceContainer


class TraceCore:
    """Main controller."""

    def __init__(self):
        self.config = ConfigManager()
        self.plugins = PluginManager()
        self.services = ServiceContainer(self.plugins)
        self.events = EventBus()

    def start(self):
        logger.info("Starting TRACE...")

        cfg = self.config.load()

        self.plugins.load_plugins()

        self.events.publish("TRACE_STARTED")


        print()
        print("TRACE is running.")
        print(cfg)
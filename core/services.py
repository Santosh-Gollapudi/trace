from services.search_service import SearchService
from services.memory_service import MemoryService
from services.plugin_service import PluginService
from services.system_service import SystemService


class ServiceContainer:

    def __init__(self, plugin_manager):

        self.search = SearchService()
        self.memory = MemoryService()
        self.plugins = PluginService(plugin_manager)
        self.system = SystemService()
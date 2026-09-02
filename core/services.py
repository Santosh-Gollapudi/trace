from services.search_service import SearchService
from services.memory_service import MemoryService
from services.plugin_service import PluginService
from services.system_service import SystemService
from services.filesystem_service import FileSystemService
from services.network_service import NetworkService
from services.process_service import ProcessService
from services.power_service import PowerService

class ServiceContainer:

    def __init__(self, plugin_manager):

        self.search = SearchService()
        self.memory = MemoryService()
        self.plugins = PluginService(plugin_manager)
        self.system = SystemService()
        self.filesystem = FileSystemService()
        self.network = NetworkService()
        self.process = ProcessService()
        self.power = PowerService()
        self.network = NetworkService()

from services.service import BaseService


class PluginService(BaseService):

    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager

    def list_plugins(self):
        return self.plugin_manager.list_plugins()
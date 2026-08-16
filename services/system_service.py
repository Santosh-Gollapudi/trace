from services.service import BaseService
from platforms.platform import get_system


class SystemService(BaseService):

    def __init__(self):
        self.system = get_system()

    def pwd(self):
        return self.system.pwd()

    def cd(self, path):
        return self.system.cd(path)
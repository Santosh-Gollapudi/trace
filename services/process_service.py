from services.service import BaseService
from platforms.platform import get_process


class ProcessService(BaseService):

    def __init__(self):
        self.process = get_process()

    def list_processes(self):
        return self.process.list_processes()

    def kill(self, pid):
        return self.process.kill(pid)
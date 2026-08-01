from abc import ABC, abstractmethod


class ProcessInterface(ABC):

    @abstractmethod
    def list_processes(self):
        pass

    @abstractmethod
    def kill(self, pid):
        pass
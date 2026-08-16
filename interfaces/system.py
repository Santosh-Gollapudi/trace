from abc import ABC, abstractmethod


class SystemInterface(ABC):

    @abstractmethod
    def pwd(self):
        pass

    @abstractmethod
    def cd(self, path):
        pass
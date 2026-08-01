from abc import ABC, abstractmethod


class PowerInterface(ABC):

    @abstractmethod
    def battery(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
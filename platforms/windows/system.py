from abc import ABC, abstractmethod


class SystemInterface(ABC):

    @abstractmethod
    def execute(self, command: str):
        pass
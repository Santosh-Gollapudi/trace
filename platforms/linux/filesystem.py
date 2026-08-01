from abc import ABC, abstractmethod


class FileSystemInterface(ABC):

    @abstractmethod
    def list_directory(self, path):
        pass

    @abstractmethod
    def exists(self, path):
        pass
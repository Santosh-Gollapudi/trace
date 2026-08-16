from abc import ABC, abstractmethod


class FileSystemInterface(ABC):

    @abstractmethod
    def list_directory(self, path):
        pass

    @abstractmethod
    def exists(self, path):
        pass

    @abstractmethod
    def mkdir(self, path):
        pass

    @abstractmethod
    def touch(self, path):
        pass

    @abstractmethod
    def read(self, path):
        pass

    @abstractmethod
    def write(self, path, text):
        pass

    @abstractmethod
    def append(self, path, text):
        pass
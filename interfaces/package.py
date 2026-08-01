from abc import ABC, abstractmethod


class PackageInterface(ABC):

    @abstractmethod
    def install(self, package):
        pass

    @abstractmethod
    def remove(self, package):
        pass
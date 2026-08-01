from abc import ABC, abstractmethod


class NetworkInterface(ABC):

    @abstractmethod
    def scan_wifi(self):
        pass

    @abstractmethod
    def current_ip(self):
        pass
import socket
from interfaces.network import NetworkInterface


class WindowsNetwork(NetworkInterface):

    def scan_wifi(self):
        return []

    def current_ip(self):
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
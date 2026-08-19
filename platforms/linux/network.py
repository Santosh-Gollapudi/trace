import socket
from interfaces.network import NetworkInterface


class LinuxNetwork(NetworkInterface):

    def scan_wifi(self):
        return []

    def current_ip(self):
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
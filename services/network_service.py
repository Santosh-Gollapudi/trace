from services.service import BaseService
from platforms.platform import get_network


class NetworkService(BaseService):

    def __init__(self):
        self.network = get_network()

    def current_ip(self):
        return self.network.current_ip()

    def scan_wifi(self):
        return self.network.scan_wifi()
from services.service import BaseService
from platforms.platform import get_power


class PowerService(BaseService):

    def __init__(self):
        self.power = get_power()

    def battery(self):
        return self.power.battery()

    def shutdown(self):
        return self.power.shutdown()
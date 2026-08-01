from services.service import BaseService


class MemoryService(BaseService):

    def save(self, key, value):
        raise NotImplementedError

    def load(self, key):
        raise NotImplementedError
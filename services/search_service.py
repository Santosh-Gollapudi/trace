from services.service import BaseService


class SearchService(BaseService):

    def search(self, query: str):
        raise NotImplementedError
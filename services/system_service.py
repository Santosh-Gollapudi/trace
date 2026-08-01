class SystemService(BaseService):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def exists(self, path):
        return self.filesystem.exists(path)
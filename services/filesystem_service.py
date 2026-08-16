from services.service import BaseService
from platforms.platform import get_filesystem
class FileSystemService(BaseService):

    def __init__(self):
        self.filesystem = get_filesystem()

    def list_directory(self, path):
        return self.filesystem.list_directory(path)

    def exists(self, path):
        return self.filesystem.exists(path)

    def mkdir(self, path):
        return self.filesystem.mkdir(path)

    def touch(self, path):
        return self.filesystem.touch(path)

    def read(self, path):
        return self.filesystem.read(path)

    def write(self, path, text):
        return self.filesystem.write(path, text)

    def append(self, path, text):
        return self.filesystem.append(path, text)
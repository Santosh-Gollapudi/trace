from services.service import BaseService
from platforms.platform import get_package


class PackageService(BaseService):

    def __init__(self):
        self.package = get_package()

    def install(self, package):
        return self.package.install(package)

    def remove(self, package):
        return self.package.remove(package)
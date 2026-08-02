from services.service import BaseService
from pathlib import Path

class SystemService(BaseService):

    def __init__(self):

        self.current_directory = Path.cwd()
        
    def pwd(self):
        return self.current_directory

    def ls(self):
        return list(self.current_directory.iterdir())
    
    def exists(self, name):
        return (self.current_directory / name).exists()
    
    def cd(self, path):

        new_path = (self.current_directory / path).resolve()

        if new_path.exists() and new_path.is_dir():
            self.current_directory = new_path
            return True
        return False
    
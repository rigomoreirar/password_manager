from abc import ABC, abstractmethod

class FileUploaderPort(ABC):
    @abstractmethod
    def upload_file(self, folder_name):
        pass

from abc import ABC, abstractmethod

class FileUploaderPort(ABC):
    @abstractmethod
    def upload_file(self, file_path, folder_name):
        pass

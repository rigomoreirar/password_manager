from abc import ABC, abstractmethod

class PasswordGeneratorPort(ABC):
    @abstractmethod
    def generate_password(self):
        pass

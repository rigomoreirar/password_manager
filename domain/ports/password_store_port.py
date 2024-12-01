from abc import ABC, abstractmethod
from ..models.password_entry import PasswordEntry

class PasswordStorePort(ABC):
    @abstractmethod
    def add_password(self, PasswordEntry: PasswordEntry):
        pass

    @abstractmethod
    def update_password(self, PasswordEntry: PasswordEntry):
        pass

    @abstractmethod
    def get_password(self, username):
        pass

    @abstractmethod
    def get_all_usernames(self):
        pass

    @abstractmethod
    def get_all_passwords(self):
        pass

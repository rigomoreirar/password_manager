from abc import ABC, abstractmethod
from ..models.password_entry_model import PasswordEntryModel

class PasswordStorePort(ABC):
    @abstractmethod
    def add_password(self, PasswordEntry: PasswordEntryModel):
        pass

    @abstractmethod
    def update_password(self, PasswordEntry: PasswordEntryModel):
        pass

    @abstractmethod
    def get_password(self, username):
        pass

    @abstractmethod
    def get_all_usernames(self):
        pass
    
    @abstractmethod
    def get_all_in_domain(self, domain):
        pass

    @abstractmethod
    def get_all_passwords(self):
        pass


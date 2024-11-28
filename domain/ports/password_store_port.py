from abc import ABC, abstractmethod

class PasswordStorePort(ABC):
    @abstractmethod
    def add_password(self, username, password):
        pass

    @abstractmethod
    def update_password(self, username, password):
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

from .base_command import BaseCommand
from domain.services.password_service import PasswordService
from domain.models.password_entry_model import PasswordEntryModel

class NewPasswordCommand(BaseCommand):
    def __init__(self, username, domain, password_generator, password_store, password=None):
        self.username = username
        self.domain = domain
        self.password = password
        self.password_service = PasswordService(password_store, password_generator)

    def execute(self):
        print(f"Creating a new password for username: {self.username}. In domain: {self.domain}.")
        try:
            if self.password:
                password_entry = PasswordEntryModel(username=self.username, password=self.password, domain=self.domain)
                add_password = self.password_service.add_existing_password(password_entry)
                print(f"Added existing password: {add_password}")
            else:
                add_password = self.password_service.create_password(self.username, self.domain)
                print(f"Generated password: {add_password}")
            print(f"Password stored successfully for username: {self.username}.")
        except Exception as e:
            print(f"An error occurred: {e}")
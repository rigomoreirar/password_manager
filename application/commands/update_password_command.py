from .base_command import BaseCommand
from domain.services.password_service import PasswordService 

class UpdatePasswordCommand(BaseCommand):
    def __init__(self, username, domain, password_generator, password_store):
        self.username = username
        self.domain = domain
        self.password_service = PasswordService(password_store, password_generator)

    def execute(self):
        print(f"Updating password for username: {self.username}. In domain: {self.domain}.")
        try:
            password = self.password_service.update_password(self.username, self.domain)
            print(f"Generated updated password: {password}")
            print(f"Password updated successfully for username: {self.username}.")
        except Exception as e:
            print(f"An error occurred: {e}")
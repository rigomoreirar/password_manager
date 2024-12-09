from .base_command import BaseCommand
from domain.services.password_service import PasswordService

class DeletePasswordCommand(BaseCommand):
    def __init__(self, username, domain, password_store):
        self.username = username
        self.domain = domain
        self.password_service = PasswordService(password_store, None)
        
    def execute(self):
        try:
            print(f"Deleting password for username: {self.username}. In domain: {self.domain}.")
            self.password_service.delete_password(self.username, self.domain)
            print(f"Password deleted successfully for username: {self.username}.")
        except Exception as e:
            print(f"An error occurred: {e}")
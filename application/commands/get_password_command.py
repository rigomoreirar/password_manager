from .base_command import BaseCommand
from domain.services.password_service import PasswordService
import pprint

class GetPasswordCommand(BaseCommand):
    def __init__(self, username, all_option, password_store):
        self.username = username
        self.all_option = all_option
        self.password_service = PasswordService(password_store, None)

    def execute(self):
        try:
            if self.username:
                print(f"Retrieving password for username: {self.username}.")
                password = self.password_service.retrieve_password(self.username)
                print(f"Password for username '{self.username}': {password}")
            elif self.all_option == "usernames":
                print("Retrieving all usernames.")
                all_usernames = self.password_service.retrieve_all_usernames()
                pprint.pprint({"All Usernames": all_usernames})
            elif self.all_option == "passwords":
                print("Retrieving all passwords.")
                all_passwords = self.password_service.retrieve_all_passwords()
                pprint.pprint({"All Passwords": all_passwords})
            else:
                print("Invalid get command.")
        except Exception as e:
            print(f"An error occurred: {e}")

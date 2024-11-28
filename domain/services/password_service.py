from ..ports.password_store_port import PasswordStorePort
from ..ports.password_generator_port import PasswordGeneratorPort

class PasswordService:
    def __init__(self, password_store: PasswordStorePort, password_generator: PasswordGeneratorPort):
        self.password_store = password_store
        self.password_generator = password_generator

    def create_password(self, username):
        password = self.password_generator.generate_password()
        self.password_store.add_password(username, password)
        return password

    def update_password(self, username):
        password = self.password_generator.generate_password()
        self.password_store.update_password(username, password)
        return password

    def retrieve_password(self, username):
        return self.password_store.get_password(username)

    def retrieve_all_usernames(self):
        return self.password_store.get_all_usernames()

    def retrieve_all_passwords(self):
        return self.password_store.get_all_passwords()

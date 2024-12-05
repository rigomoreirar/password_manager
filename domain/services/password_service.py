from ..ports.password_store_port import PasswordStorePort
from ..ports.password_generator_port import PasswordGeneratorPort
from ..models.password_entry_model import PasswordEntryModel

class PasswordService:
    def __init__(self, password_store: PasswordStorePort, password_generator: PasswordGeneratorPort):
        self.password_store = password_store
        self.password_generator = password_generator

    def create_password(self, username, domain):
        password = self.password_generator.generate_password()
        password_entry = PasswordEntryModel(username, password, domain)
        self.password_store.add_password(password_entry)
        return password_entry

    def update_password(self, username, domain):
        password = self.password_generator.generate_password()
        password_entry = PasswordEntryModel(username, password, domain)
        self.password_store.update_password(password_entry)
        return password_entry

    def retrieve_password(self, username, domain):
        return self.password_store.get_password(username, domain)

    def retrieve_all_usernames(self):
        return self.password_store.get_all_usernames()

    def retrieve_all_in_domain(self, domain):
        return self.password_store.get_all_in_domain(domain)

    def retrieve_all_passwords(self):
        return self.password_store.get_all_passwords()

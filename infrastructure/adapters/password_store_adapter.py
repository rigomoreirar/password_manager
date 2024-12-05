from domain.ports.password_store_port import PasswordStorePort
from domain.models.password_entry_model import PasswordEntryModel

class PasswordStoreAdapter(PasswordStorePort):
    def __init__(self, file_path="passwords.txt"):
        self.file_path = file_path

    def add_password(self, password_entry: PasswordEntryModel):
        with open(self.file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                stored_username, stored_password, stored_domain = line.strip().split("|")
                if stored_domain == password_entry.domain and stored_username == password_entry.username:
                    raise ValueError(
                        f"Username '{password_entry.username}' already exists in the domain '{password_entry.domain}'.")

        with open(self.file_path, "a") as f:
            f.write(f"{password_entry.username}|{password_entry.password}|{password_entry.domain}\n")

    def update_password(self, password_entry: PasswordEntryModel):
        updated = False
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        with open(self.file_path, "w") as f:
            for line in lines:
                stored_username, stored_password, stored_domain = line.strip().split("|")
                if stored_username == password_entry.username and stored_domain == password_entry.domain:
                    f.write(f"{password_entry.username}|{password_entry.password}|{password_entry.domain}\n")
                    updated = True
                else:
                    f.write(line)

        if not updated:
            raise ValueError(
                f"Username '{password_entry.username}' with domain '{password_entry.domain}' not found in the store.")

    def get_password(self, username, domain):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            stored_username, stored_password, stored_domain = line.strip().split("|")
            if stored_username == username and stored_domain == domain:
                return stored_password

        raise ValueError(f"Username '{username}' with domain '{domain}' not found in the store.")

    def get_all_usernames(self):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        usernames = set()
        for line in lines:
            stored_username, stored_password, stored_domain = line.strip().split("|")
            usernames.add((stored_username, stored_domain))

        return list(usernames)

    def get_all_in_domain(self, domain):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        entries = []
        for line in lines:
            stored_username, stored_password, stored_domain = line.strip().split("|")
            if stored_domain == domain:
                entries.append({"username": stored_username, "password": stored_password})

        return entries

    def get_all_passwords(self):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        return [{"username": line.strip().split("|")[0], "password": line.strip().split("|")[1], "domain": line.strip().split("|")[2]} for line in lines]
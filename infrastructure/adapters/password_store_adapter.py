from domain.ports.password_store_port import PasswordStorePort
from domain.models.password_entry import PasswordEntry

class PasswordStoreAdapter(PasswordStorePort):
    def __init__(self, file_path="passwords.txt"):
        self.file_path = file_path

    def add_password(self, password_entry: PasswordEntry):
        with open(self.file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                stored_username, _ = line.strip().split("|")
                if stored_username == password_entry.username:
                    raise ValueError(
                        f"Username '{password_entry.username}' already exists in the store.")

        with open(self.file_path, "a") as f:
            f.write(f"{password_entry.username}|{password_entry.password}\n")

    def update_password(self, password_entry: PasswordEntry):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        with open(self.file_path, "w") as f:
            for line in lines:
                stored_username, _ = line.strip().split("|")
                if stored_username == password_entry.username:
                    f.write(f"{password_entry.username}|{password_entry.password}\n")
                else:
                    f.write(line)

    def get_password(self, username):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            stored_username, stored_password = line.strip().split("|")
            if stored_username == username:
                return stored_password

        raise ValueError(f"Username '{username}' not found in the store.")

    def get_all_usernames(self):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        return [line.strip().split("|")[0] for line in lines]

    def get_all_passwords(self):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        return [{"username": line.strip().split("|")[0], "password": line.strip().split("|")[1]} for line in lines]

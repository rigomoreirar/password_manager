import os


class PasswordStore:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def add_password(self, username, password):
        """
        Adds a new password with the given username to the store.
        """
        self.username = username
        self.password = password
        
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                stored_username, stored_password = line.strip().split("|")
                if stored_username == username:
                    raise ValueError(f"Username '{username}' already exists in the store.")

        with open("passwords.txt", "a") as f:
            f.write(f"{self.username}|{self.password}\n")

    def update_password(self, username, password):
        """
        Updates the password for the given username.
        """
        self.username = username
        self.password = password

        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        with open("passwords.txt", "w") as f:
            for line in lines:
                stored_username, stored_password = line.strip().split("|")
                if stored_username == username:
                    f.write(f"{self.username}|{self.password}\n")
                else:
                    f.write(line)

    def get_all_usernames(self):
        """
        Retrieves a list of all usernames from the store.
        """
        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        username_list = []

        for line in lines:
            stored_username, _ = line.strip().split("|")
            username_list.append(stored_username)

        return username_list

    def get_password(self, username):
        """
        Retrieves the password for a specific username.
        """
        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        password = ""

        for line in lines:
            stored_username, stored_password = line.strip().split("|")
            if stored_username == username:
                password = stored_password

        return password

    def get_all_passwords(self):
        """
        Retrieves all usernames and passwords as a list of dictionaries.
        """
        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        all_passwords = []

        for line in lines:
            stored_username, stored_password = line.strip().split("|")
            all_passwords.append({"username": stored_username, "password": stored_password})

        return all_passwords


if __name__ == "__main__":
    test = PasswordStore()

    # Example usage
    test.add_password("john_doe", "password123")
    test.add_password("jane_doe", "securepass456")

    print("All Usernames:", test.get_all_usernames())
    print("Password for 'john_doe':", test.get_password("john_doe"))
    print("All passwords:", test.get_all_passwords())

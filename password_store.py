import os


class PasswordStore:
    def __init__(self, id="", password=""):
        self.id = id
        self.password = password

    def add_password(self, id, password):
        """
        Adds a new password with the given ID to the store.
        """
        self.id = id
        self.password = password
        
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                stored_id, stored_password = line.strip().split("|")
                if stored_id == id:
                    raise ValueError(f"ID '{id}' already exists in the store.")
            

        with open("passwords.txt", "a") as f:
            f.write(f"{self.id}|{self.password}\n")

    def update_password(self, id, password):
        """
        Updates the password for the given ID.
        """
        self.id = id
        self.password = password

        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        with open("passwords.txt", "w") as f:
            for line in lines:
                stored_id, stored_password = line.strip().split("|")
                if stored_id == id:
                    f.write(f"{self.id}|{self.password}\n")
                else:
                    f.write(line)

    def get_all_id(self):
        """
        Retrieves a list of all IDs from the store.
        """
        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        id_list = []

        for line in lines:
            stored_id, stored_password = line.strip().split("|")
            id_list.append(stored_id)

        return id_list

    def get_password(self, id):
        """
        Retrieves the password for a specific ID.
        """
        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        password = ""

        for line in lines:
            stored_id, stored_password = line.strip().split("|")
            if stored_id == id:
                password = stored_password

        return password

    def get_all_passwords(self):
        """
        Retrieves all IDs and passwords as a list of dictionaries.
        """
        with open("passwords.txt", "r") as f:
            lines = f.readlines()

        all_passwords = []

        for line in lines:
            stored_id, stored_password = line.strip().split("|")
            all_passwords.append({"id": stored_id, "password": stored_password})

        return all_passwords


if __name__ == "__main__":
    test = PasswordStore()

    # Example usage
    test.add_password("email", "password123")
    test.add_password("bank", "securepass456")

    print("All IDs:", test.get_all_id())
    print("Password for 'email':", test.get_password("email"))
    print("All passwords:", test.get_all_passwords())

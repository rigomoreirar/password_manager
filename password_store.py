import os


class PasswordStore:
    def __init__(self, id="", password=""):
        self.id = id
        self.password = password

    def add_password(self, id, password):
        self.id = id
        self.password = password

        f = open("passwords.txt", "a")
        f.write(f"{self.id}|{self.password}\n")
        f.close()

    def update_password(self, id, password):
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
        f = open("passwords.txt", "r")
        lines = f.readlines()

        id_list = []

        for line in lines:
            stored_id, stored_password = line.strip().split("|")
            id_list.append(stored_id)

        return id_list

    def get_password(self, id):
        f = open("passwords.txt", "r")
        lines = f.readlines()

        password = ""

        for line in lines:
            stored_id, stored_password = line.strip().split("|")
            if stored_id == id:
                password = stored_password

        return password


if __name__ == "__main__":
    test = PasswordStore()

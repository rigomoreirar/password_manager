import hashlib
import random
import string


class PasswordGenerator:
    def __init__(self, seed=None, options="", length=15):
        self.seed = seed
        self.options = options
        self.length = length

    def generate_password(self):
        random.seed(self.seed)

        if self.options == "no_special_chars":
            characters = string.ascii_letters + string.digits
        else:
            characters = string.ascii_letters + string.digits + "#-$"

        password = ''.join(random.choice(characters)
                           for _ in range(self.length))

        return password


if __name__ == "__main__":
    seed = "my_secret_key"
    test = PasswordGenerator(seed=seed)
    print(test.generate_password())

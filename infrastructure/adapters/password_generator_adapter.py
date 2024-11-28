from domain.ports.password_generator_port import PasswordGeneratorPort
import random
import string

class PasswordGeneratorAdapter(PasswordGeneratorPort):
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

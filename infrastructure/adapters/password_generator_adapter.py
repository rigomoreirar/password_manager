from domain.ports.password_generator_port import PasswordGeneratorPort
import random
import string

class PasswordGeneratorAdapter(PasswordGeneratorPort):
    def __init__(self, seed=None, options="", length=15):
        self.seed = seed
        self.options = options
        self.length = length

    def generate_password(self):
        if self.length < 4:
            raise ValueError("Password length must be at least 4 to include all required character types.")
        
        random.seed(self.seed)

        uppercase_chars = string.ascii_uppercase
        lowercase_chars = string.ascii_lowercase
        digits = string.digits
        special_chars = "#-$" if self.options != "no_special_chars" else ""

        if not special_chars and self.options == "no_special_chars":
            characters = uppercase_chars + lowercase_chars + digits
        else:
            characters = uppercase_chars + lowercase_chars + digits + special_chars

        # Ensure each required character type is included
        password = [
            random.choice(uppercase_chars),
            random.choice(lowercase_chars),
            random.choice(digits)
        ]

        if special_chars:
            password.append(random.choice(special_chars))

        # Fill the remaining length with random choices from the allowed characters
        if self.length > len(password):
            password += random.choices(characters, k=self.length - len(password))

        # Shuffle to prevent predictable sequences
        random.shuffle(password)

        return ''.join(password)

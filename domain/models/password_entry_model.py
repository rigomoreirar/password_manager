class PasswordEntryModel:
    def __init__(self, username, password, domain):
        self.username = username
        self.password = password
        self.domain = domain

    def __repr__(self):
        return f"PasswordEntryModel(username='{self.username}', password='{self.password}', domain='{self.domain}')"
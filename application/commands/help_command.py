from .base_command import BaseCommand


class HelpCommand(BaseCommand):
    def execute(self):
        print(
            """
Password Manager Help:

Commands:
  -help             Display this help message with detailed usage instructions.

  -new              Create a new password. Requires the following:
                      -domain    (required) The domain for the site which corresponds to the username.
                      -username  (Required) The unique username for the password.
                      -type      (Optional) The type of the password (e.g., email, banking).
                      -seed      (Optional) A specific seed for generating the password.

  -update           Update an existing password. Requires:
                      -domain      (required) The domain for the site which corresponds to the username.
                      -username    (Required) The unique username of the password to update.
                      -type        (Optional) The type of the new password.
                      -seed        (Optional) A specific seed for generating the new password.

  -get              Retrieve passwords. Requires one of the following:
                      -doamin, -username   (Retrieve the passwords for a specific username in a domain).
                      -all domain          (Retrieve all stored usernames and paddwords which correspond to the domain).
                      -all usernames       (Retrieve all stored usernames and their respective domains).
                      -all passwords       (Retrieve all stored passwords, usernames, and domains).

  -upload           Upload all passwords to Google Drive.
  

Examples:
  Create a new password:
    python argument_handler.py -new -domain example.com -username my_email -type email -seed myseed

  Update an existing password:
    python argument_handler.py -update -domain example.com -username my_email -type email -seed mynewseed

  Retrieve a specific password:
    python argument_handler.py -get -domain example.com -username my_email

  Retrieve all usernames and domains:
    python argument_handler.py -get -all usernames

  Retrieve all passwords, usernames, and domains:
    python argument_handler.py -get -all passwords

  Upload all passwords to Google Drive:
    python argument_handler.py -upload
""")
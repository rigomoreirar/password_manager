from .base_command import BaseCommand


class HelpCommand(BaseCommand):
    def execute(self):
        print(
            """
Password Manager Help:

Commands:
  -help             Display this help message with detailed usage instructions.

  -new              Create a new password. Requires the following:
                      -id    (Required) The unique ID for the password.
                      -type  (Optional) The type of the password (e.g., email, banking).
                      -seed  (Optional) A specific seed for generating the password.

  -update           Update an existing password. Requires:
                      -id    (Required) The unique ID of the password to update.
                      -type  (Optional) The type of the new password.
                      -seed  (Optional) A specific seed for generating the new password.

  -get              Retrieve passwords. Requires one of the following:
                      -id            (Retrieve the password for a specific ID).
                      -all ids       (Retrieve all stored IDs).
                      -all passwords (Retrieve all stored passwords).

  -upload           Upload all passwords to Google Drive.

Examples:
  Create a new password:
    python argument_handler.py -new -id my_email -type email -seed myseed

  Update an existing password:
    python argument_handler.py -update -id my_email -type email -seed mynewseed

  Retrieve a specific password:
    python argument_handler.py -get -id my_email

  Retrieve all IDs:
    python argument_handler.py -get -all ids

  Retrieve all passwords:
    python argument_handler.py -get -all passwords

  Upload all passwords to Google Drive:
    python argument_handler.py -upload
""")
import argparse


class ArgumentHandler:
    def __init__(self):
        """
        Initializes the argument dictionary to store parsed argument values.
        """
        self.arguments = {
            "help": False,
            "new": {"id": None, "type": None, "seed": None},
            "get": {"id": None, "all": None},
            "update": {"id": None, "type": None, "seed": None},
            "upload": False,
            "Error": None,  # Error messages or None if no error
        }

    def handle_arguments(self):
        """
        Parses command-line arguments and populates the argument dictionary.
        Ensures proper validation of required dependencies for each action.
        Returns:
            dict: The populated argument dictionary.
        """
        # Initialize the parser
        parser = argparse.ArgumentParser(
            description="Password Manager: A tool to manage your passwords with multiple options for creation, retrieval, and updating."
        )

        # Create a mutually exclusive group for the main actions
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-help", action="store_true",
                           help="Display detailed help information about possible commands and their usage.")
        group.add_argument("-new", action="store_true",
                           help="Create a new password. Requires -id and optionally -type.")
        group.add_argument("-get", action="store_true",
                           help="Get passwords. Requires -id for a specific password or -all for either IDs or passwords.")
        group.add_argument("-upload", action="store_true",
                           help="Upload to Google Drive the current passwords.")
        group.add_argument("-update", action="store_true",
                           help="Update a password. Requires -id and optionally -type.")

        # Additional arguments for get, new, and update
        parser.add_argument(
            "-id", type=str, help="Specify the ID for the action."
        )
        parser.add_argument(
            "-all", type=str, choices=["ids", "passwords"],
            help="Retrieve all IDs or all passwords (used with -get). Choices: 'ids', 'passwords'."
        )
        parser.add_argument(
            "-type", type=str, help="Specify if the password should have special characters."
        )
        parser.add_argument(
            "-seed", type=str, help="Generate a password using a specific seed."
        )

        # Parse the arguments
        args = parser.parse_args()

        # Handle each action
        if args.help:
            self.arguments.update({"help": True})
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
"""
            )

        elif args.new:
            if not args.id:
                self.arguments.update(
                    {"Error": "Creating a new password requires the -id argument."})
            else:
                self.arguments["new"].update(
                    {"id": args.id, "type": args.type or "default", "seed": args.seed})

        elif args.update:
            if not args.id:
                self.arguments.update(
                    {"Error": "Updating a password requires the -id argument."})
            else:
                self.arguments["update"].update(
                    {"id": args.id, "type": args.type or "default", "seed": args.seed})

        elif args.get:
            if args.id and args.all:
                self.arguments.update(
                    {"Error": "Conflicting arguments: Use either -id or -all with -get, but not both."})
            elif args.all:
                self.arguments["get"].update({"all": args.all})
            elif args.id:
                self.arguments["get"].update({"id": args.id})
            else:
                self.arguments.update(
                    {"Error": "Getting passwords requires either -id or -all."})

        elif args.upload:
            self.arguments.update({"upload": True})

        else:
            self.arguments.update(
                {"Error": "No valid arguments provided. Use -help to see the list of possible actions."})

        return self.arguments


if __name__ == "__main__":
    handler = ArgumentHandler()
    result = handler.handle_arguments()
    print(result)  # Prints the JSON-like dictionary

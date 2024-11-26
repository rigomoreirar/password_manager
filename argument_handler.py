import argparse


class ArgumentHandler:
    def __init__(self):
        """
        Initializes the argument dictionary to store parsed argument values.
        """
        self.arguments = {
            "help": False,
            "new": {"id": None, "type": None},
            "get": {"id": None},
            "list": {"passwords": False},
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
            description="Password Manager: A tool to manage your passwords with multiple options for creation, retrieval, and listing."
        )

        # Create a mutually exclusive group for the main actions
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-help", action="store_true",
                           help="Display detailed help information about possible commands and their usage.")
        group.add_argument("-new", action="store_true",
                           help="Create a new password. Requires -id and optionally -type.")
        group.add_argument("-get", action="store_true",
                           help="Get a password by its ID. Requires -id.")
        group.add_argument("-list", action="store_true",
                           help="List all stored IDs. Use with -passwords to include passwords.")
        group.add_argument("-passwords", action="store_true",
                           help="List all stored IDs and their corresponding passwords.")

        # Additional arguments
        parser.add_argument(
            "-id", type=str, help="Specify the ID for the action.")
        parser.add_argument(
            "-type", type=str, help="Specify the type of the password (e.g., email, banking).")

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

  -get              Retrieve a password by ID. Requires:
                      -id    (Required) The unique ID of the password to retrieve.

  -list             List all stored IDs. Optional:
                      -passwords   Include the corresponding passwords in the listing.

  -passwords        List all stored IDs along with their passwords.

Examples:
  Create a new password:
    python argument_handler.py -new -id my_email -type email

  Retrieve a password:
    python argument_handler.py -get -id my_email

  List all IDs:
    python argument_handler.py -list

  List all IDs with passwords:
    python argument_handler.py -list -passwords
"""
            )

        elif args.new:
            if not args.id:
                self.arguments.update(
                    {"Error": "Creating a new password requires the -id argument."})
            else:
                self.arguments["new"].update(
                    {"id": args.id, "type": args.type or "default"})
                if args.type and args.type != "no_special_chars":
                    self.arguments.update(
                        {"Error": "Invalid password type. Use 'no_special_chars' for a password without special characters."})

        elif args.get:
            if not args.id:
                self.arguments.update(
                    {"Error": "Getting a password requires the -id argument."})
            else:
                self.arguments["get"].update({"id": args.id})

        elif args.list:
            self.arguments["list"].update({"passwords": args.passwords})

        elif args.passwords:
            self.arguments["list"].update({"passwords": True})

        else:
            self.arguments.update(
                {"Error": "No valid arguments provided. Use -help to see the list of possible actions."})

        return self.arguments


if __name__ == "__main__":
    handler = ArgumentHandler()
    result = handler.handle_arguments()
    print(result)  # Prints the JSON-like dictionary

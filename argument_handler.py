import argparse


class ArgumentHandler:
    def __init__(self):
        """
        Initializes the argument dictionary to store parsed argument values.
        """
        self.arguments = {
            "help": False,
            "new": {"username": None, "type": None, "seed": None},
            "get": {"username": None, "all": None},
            "update": {"username": None, "type": None, "seed": None},
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
                           help="Create a new password. Requires -username and optionally -type.")
        group.add_argument("-get", action="store_true",
                           help="Get passwords. Requires -username for a specific password or -all for either usernames or passwords.")
        group.add_argument("-upload", action="store_true",
                           help="Upload to Google Drive the current passwords.")
        group.add_argument("-update", action="store_true",
                           help="Update a password. Requires -username and optionally -type.")

        # Additional arguments for get, new, and update
        parser.add_argument(
            "-username", type=str, help="Specify the username for the action."
        )
        parser.add_argument(
            "-all", type=str, choices=["usernames", "passwords"],
            help="Retrieve all usernames or all passwords (used with -get). Choices: 'usernames', 'passwords'."
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
        elif args.new:
            if not args.username:
                self.arguments.update(
                    {"Error": "Creating a new password requires the -username argument."})
            else:
                self.arguments["new"].update(
                    {"username": args.username, "type": args.type or "default", "seed": args.seed})
        elif args.update:
            if not args.username:
                self.arguments.update(
                    {"Error": "Updating a password requires the -username argument."})
            else:
                self.arguments["update"].update(
                    {"username": args.username, "type": args.type or "default", "seed": args.seed})
        elif args.get:
            if args.username and args.all:
                self.arguments.update(
                    {"Error": "Conflicting arguments: Use either -username or -all with -get, but not both."})
            elif args.all:
                self.arguments["get"].update({"all": args.all})
            elif args.username:
                self.arguments["get"].update({"username": args.username})
            else:
                self.arguments.update(
                    {"Error": "Getting passwords requires either -username or -all."})
        elif args.upload:
            self.arguments.update({"upload": True})
        else:
            self.arguments.update(
                {"Error": "No valid arguments provided. Use -help to see the list of possible actions."})

        return self.arguments

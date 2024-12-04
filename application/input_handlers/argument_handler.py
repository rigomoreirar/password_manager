import argparse
from domain.models.arguments_model import ArgumentsModel

class ArgumentHandler:
    def __init__(self):
        """
        Initializes the ArgumentHandler with an empty ArgumentsModel.
        """
        self.arguments = ArgumentsModel()

    def handle_arguments(self):
        """
        Parses command-line arguments and populates the ArgumentsModel instance.
        Returns:
            ArgumentsModel: The populated ArgumentsModel instance.
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
            "-domain", type=str, help="Specify the domain for the site which corresponds to the username."
        )
        parser.add_argument(
            "-all", type=str, choices=["usernames", "passwords", "domains"],
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
            self.arguments.help = True
        elif args.new:
            if not args.username or not args.domain:
                if not args.username:
                    self.arguments.error = "Creating a new password requires the -username argument."
                if not args.domain:
                    self.arguments.error = "Creating a new password requires the -domain argument."
            else:
                self.arguments.new.update({
                    "username": args.username,
                    "type": args.type or "default",
                    "seed": args.seed,
                    "domain": args.domain
                })
        elif args.update:
            if not args.username or not args.domain:
                if not args.username:
                    self.arguments.error = "Updating a password requires the -username argument."
                if not args.domain:
                    self.arguments.error = "Updating a password requires the -domain argument."
            else:
                self.arguments.update.update({
                    "username": args.username,
                    "type": args.type or "default",
                    "seed": args.seed,
                    "domain": args.domain
                })
        elif args.get:
            if args.username and args.all or args.domain and args.all or args.username and args.domain and args.all:
                self.arguments.error = "Conflicting arguments: Use either -domain, -username or -all with -get, but not both."
            elif args.all:
                self.arguments.get["all"] = args.all
            elif args.username or args.domain:
                if not args.domain:
                    self.arguments.error = "Getting passwords from a single username requires the -domain argument."
                elif not args.username:
                    self.arguments.error = "Getting passwords from a single username with a corresponding domain requires the -username argument."
                else:
                    self.arguments.get["username"] = args.username
                    self.arguments.get["domain"] = args.domain
            else:
                self.arguments.error = "Getting passwords requires either -domain, -username or -all."
        elif args.upload:
            self.arguments.upload = True
        else:
            self.arguments.error = "No valid arguments provided. Use -help to see the list of possible actions."

        return self.arguments

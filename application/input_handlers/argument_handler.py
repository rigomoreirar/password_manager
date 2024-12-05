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
        parser = self._initialize_parser()
        args = parser.parse_args()
        self._handle_action(args)
        return self.arguments

    def _initialize_parser(self):
        """
        Initializes the argument parser with the required arguments.
        Returns:
            ArgumentParser: The initialized argument parser.
        """
        parser = argparse.ArgumentParser(
            description="Password Manager: A tool to manage your passwords with multiple options for creation, retrieval, and updating."
        )

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-help", action="store_true", help="Display detailed help information about possible commands and their usage.")
        group.add_argument("-new", action="store_true", help="Create a new password. Requires -username and optionally -type.")
        group.add_argument("-get", action="store_true", help="Get passwords. Requires -username for a specific password or -all for either usernames or passwords.")
        group.add_argument("-upload", action="store_true", help="Upload to Google Drive the current passwords.")
        group.add_argument("-update", action="store_true", help="Update a password. Requires -username and optionally -type.")

        parser.add_argument("-username", type=str, help="Specify the username for the action.")
        parser.add_argument("-domain", type=str, help="Specify the website domain.")
        parser.add_argument("-all", type=str, choices=["usernames", "passwords", "domain"], help="Retrieve all usernames or all passwords (used with -get). Choices: 'usernames', 'passwords', 'domain'.")
        parser.add_argument("-type", type=str, help="Specify if the password should have special characters.")
        parser.add_argument("-seed", type=str, help="Generate a password using a specific seed.")

        return parser

    def _handle_action(self, args):
        """
        Handles the action specified by the parsed arguments.
        Args:
            args (Namespace): The parsed arguments.
        """
        if args.help:
            self.arguments.help = True
        elif args.new:
            self._handle_new(args)
        elif args.update:
            self._handle_update(args)
        elif args.get:
            self._handle_get(args)
        elif args.upload:
            self.arguments.upload = True
        else:
            self.arguments.error = "No valid arguments provided. Use -help to see the list of possible actions."

    def _handle_new(self, args):
        """
        Handles the creation of a new password.
        Args:
            args (Namespace): The parsed arguments.
        """
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

    def _handle_update(self, args):
        """
        Handles the updating of a password.
        Args:
            args (Namespace): The parsed arguments.
        """
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

    def _handle_get(self, args):
        """
        Handles the retrieval of passwords.
        Args:
            args (Namespace): The parsed arguments.
        """
        if args.username and args.all or args.username and args.domain and args.all:
            self.arguments.error = "Conflicting arguments: Use either -domain, -username or -all or -all -domain with -get."
        elif args.all:
            if args.all == "domain":
                if not args.domain:
                    self.arguments.error = "Getting all passwords for a domain requires the -domain argument."
                else:
                    self.arguments.get["domain"] = args.domain
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

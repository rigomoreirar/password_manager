import argparse
from domain.models.arguments_model import ArgumentsModel

class ArgumentHandler:
    def __init__(self):
        self.arguments = ArgumentsModel()

    def handle_arguments(self):
        parser = self._initialize_parser()
        args = parser.parse_args()
        self._handle_action(args)
        return self.arguments

    def _initialize_parser(self):
        parser = argparse.ArgumentParser(
            description="Password Manager: A tool to manage your passwords."
        )

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-help", action="store_true", help="Display help information.")
        group.add_argument("-new", action="store_true", help="Create a new password.")
        group.add_argument("-get", action="store_true", help="Get passwords.")
        group.add_argument("-upload", action="store_true", help="Upload passwords.")
        group.add_argument("-update", action="store_true", help="Update a password.")
        group.add_argument("-delete", action="store_true", help="Delete a password.")

        parser.add_argument("-username", type=str, help="Specify the username.")
        parser.add_argument("-domain", type=str, help="Specify the website domain.")
        parser.add_argument("-all", type=str, choices=["usernames", "passwords", "domain"], help="Retrieve all entries.")
        parser.add_argument("-type", type=str, help="Specify the password type.")
        parser.add_argument("-seed", type=str, help="Generate a password using a specific seed.")
        parser.add_argument("-password", type=str, help="An existing password to add.")

        return parser

    def _handle_action(self, args):
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
        elif args.delete:
            self._handle_delete(args)
        else:
            self.arguments.error = "No valid arguments provided. Use -help to see available commands."

    def _handle_delete(self, args):
        if not args.username or not args.domain:
            self.arguments.error = "Deleting a password requires both -username and -domain arguments."
        else:
            self.arguments.delete = {
                "username": args.username,
                "domain": args.domain
            }

    def _handle_new(self, args):
        if not args.username or not args.domain:
            self.arguments.error = "Creating a new password requires both -username and -domain arguments."
        else:
            self.arguments.new.update({
                "username": args.username,
                "type": args.type or "default",
                "seed": args.seed,
                "domain": args.domain,
                "password": args.password
            })

    def _handle_update(self, args):
        if not args.username or not args.domain:
            self.arguments.error = "Updating a password requires both -username and -domain arguments."
        else:
            self.arguments.update.update({
                "username": args.username,
                "type": args.type or "default",
                "seed": args.seed,
                "domain": args.domain
            })

    def _handle_get(self, args):
        if args.username and args.all:
            self.arguments.error = "Conflicting arguments: Use either -username or -all with -get."
        elif args.all:
            if args.all == "domain" and not args.domain:
                self.arguments.error = "Retrieving all entries for a domain requires the -domain argument."
            else:
                self.arguments.get["all"] = args.all
                self.arguments.get["domain"] = args.domain
        elif args.username and args.domain:
            self.arguments.get.update({
                "username": args.username,
                "domain": args.domain
            })
        else:
            self.arguments.error = "Getting passwords requires -username and -domain, or -all with an optional -domain."
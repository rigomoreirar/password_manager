import argparse


# I want:

# -help : for listing possible actions
# -new -id -type? : for creating password
# -id -type? : for updating a password
# -get -id : for getting a password
# -list : for listing ids
# -list -passwords : for listing ids and passwords
 
class ArgumentHandler:
    def __init__(self, help=False, new=False, id="", type="", get=False, list=False, passwords=False):
        self.help = help
        self.new = new
        self.id = id
        self.type = type
        self.get = get
        self.list = list
        self.passwords = passwords
        
    def handle_arguments(self):
        
        parser = argparse.ArgumentParser(description="Password Manager")
        parser.add_argument("-help", action="store_true", help="List possible actions")
        parser.add_argument("-new", action="store_true", help="Create a new password")
        parser.add_argument("-id", type=str, help="The ID of the password to update")
        parser.add_argument("-type", type=str, help="The type of the password to update")
        parser.add_argument("-get", action="store_true", help="Get the password for the specified ID")
        parser.add_argument("-list", action="store_true", help="List all IDs")
        parser.add_argument("-passwords", action="store_true", help="List all IDs and passwords")
        
        args = parser.parse_args()
        
        if args.help:
            print("List of possible actions:")
            print("-new: Create a new password")
            print("-id: The ID of the password to update")
            print("-type: The type of the password to update")
            print("-get: Get the password for the specified ID")
            print("-list: List all IDs")
            print("-passwords: List all IDs and passwords")
        elif args.new:
            print("Creating a new password...")
        elif args.id:
            print(f"Updating password with ID {args.id}...")
        elif args.get:
            print(f"Getting password for ID {args.get}...")
        elif args.list:
            print("Listing all IDs...")
        elif args.passwords:
            print("Listing all IDs and passwords...")
        else:
            print("No valid arguments provided. Use -help to see the list of possible actions.")
        
if __name__ == "__main__":
    handler = ArgumentHandler()
    handler.handle_arguments()
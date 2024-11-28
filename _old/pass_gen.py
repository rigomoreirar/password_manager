from argument_handler import ArgumentHandler
from drive_upload import DriveUpload
from password_generator import PasswordGenerator
from password_store import PasswordStore
import pprint


def main():
    args = ArgumentHandler().handle_arguments()

    if args["Error"]:
        print(f"Error: {args['Error']}")
        return

    if args["help"]:
        print("Help command executed.")

    elif args["new"]["username"]:
        print(f"Creating a new password for username: {args['new']['username']}, Type: {args['new']['type']}, Seed: {args['new']['seed']}.")
        new_password = PasswordGenerator(seed=args["new"]["seed"], options=args["new"]["type"])
        generated_password = new_password.generate_password()
        print(f"Generated password: {generated_password}")
        try:
            password_store = PasswordStore()
            password_store.add_password(username=args["new"]["username"], password=generated_password)
            print(f"Password stored successfully for username: {args['new']['username']}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif args["update"]["username"]:
        print(f"Updating password for username: {args['update']['username']}, Type: {args['update']['type']}, Seed: {args['update']['seed']}.")
        new_password = PasswordGenerator(seed=args["update"]["seed"], options=args["update"]["type"])
        updated_password = new_password.generate_password()
        print(f"Generated updated password: {updated_password}")
        try:
            password_store = PasswordStore()
            password_store.update_password(username=args["update"]["username"], password=updated_password)
            print(f"Password updated successfully for username: {args['update']['username']}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif args["get"]["username"]:
        print(f"Retrieving password for username: {args['get']['username']}.")
        password_store = PasswordStore()
        password = password_store.get_password(username=args["get"]["username"])
        print(f"Password for username '{args['get']['username']}': {password}")

    elif args["get"]["all"] == "usernames":
        print("Retrieving all usernames.")
        password_store = PasswordStore()
        all_usernames = password_store.get_all_usernames()
        pprint.pprint({"All Usernames": all_usernames})

    elif args["get"]["all"] == "passwords":
        print("Retrieving all passwords.")
        password_store = PasswordStore()
        all_passwords = password_store.get_all_passwords()
        pprint.pprint({"All Passwords": all_passwords})

    elif args["upload"]:
        print("Uploading passwords to Google Drive.")
        try:
            uploader = DriveUpload()
            uploader.upload_file("passwords.txt", "pass_gen")
            print("Passwords uploaded successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Unknown action. Use -help to see the list of available commands.")


if __name__ == "__main__":
    main()

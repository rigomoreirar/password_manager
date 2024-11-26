from argument_handler import ArgumentHandler  # Import ArgumentHandler
from drive_upload import DriveUpload  # Import DriveUpload
from password_generator import PasswordGenerator  # Import PasswordGenerator
from password_store import PasswordStore  # Import PasswordStore
import pprint  # Import pprint for formatted output


def main():
    args = ArgumentHandler().handle_arguments()

    if args["Error"]:
        print(f"Error: {args['Error']}")
        return

    if args["help"]:
        print("Help command executed.")

    elif args["new"]["id"]:
        print(f"Creating a new password with ID: {args['new']['id']}, Type: {args['new']['type']}, Seed: {args['new']['seed']}.")

        new_password = PasswordGenerator(seed=args["new"]["seed"], options=args["new"]["type"])
        generated_password = new_password.generate_password()
        print(f"Generated password: {generated_password}")

        try:
            password_store = PasswordStore()
            password_store.add_password(id=args["new"]["id"], password=generated_password)
            print(f"Password stored successfully for ID: {args['new']['id']}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif args["update"]["id"]:
        print(f"Updating password for ID: {args['update']['id']}, Type: {args['update']['type']}, Seed: {args['update']['seed']}.")

        new_password = PasswordGenerator(seed=args["update"]["seed"], options=args["update"]["type"])
        updated_password = new_password.generate_password()
        print(f"Generated updated password: {updated_password}")

        try:
            password_store = PasswordStore()
            password_store.update_password(id=args["update"]["id"], password=updated_password)
            print(f"Password updated successfully for ID: {args['update']['id']}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif args["get"]["id"]:
        print(f"Retrieving password for ID: {args['get']['id']}.")
        password_store = PasswordStore()
        password = password_store.get_password(id=args["get"]["id"])
        print(f"Password for ID '{args['get']['id']}': {password}")

    elif args["get"]["all"] == "ids":
        print("Retrieving all IDs.")
        password_store = PasswordStore()
        all_ids = password_store.get_all_id()
        pprint.pprint({"All IDs": all_ids})

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

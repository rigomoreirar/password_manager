from argument_handler import ArgumentHandler
from application.commands.help_command import HelpCommand
from application.commands.new_password_command import NewPasswordCommand
from application.commands.update_password_command import UpdatePasswordCommand
from application.commands.get_password_command import GetPasswordCommand
from application.commands.upload_command import UploadCommand
from infrastructure.adapters.password_generator_adapter import PasswordGeneratorAdapter
from infrastructure.adapters.password_store_adapter import PasswordStoreAdapter
from infrastructure.adapters.drive_uploader_adapter import DriveUploaderAdapter

def main():
    args = ArgumentHandler().handle_arguments()

    if args["Error"]:
        print(f"Error: {args['Error']}")
        return

    command = None

    if args["help"]:
        command = HelpCommand()
    elif args["new"]["username"]:
        password_generator = PasswordGeneratorAdapter(
            seed=args["new"]["seed"],
            options=args["new"]["type"]
        )
        password_store = PasswordStoreAdapter()
        command = NewPasswordCommand(
            username=args["new"]["username"],
            password_generator=password_generator,
            password_store=password_store
        )
    elif args["update"]["username"]:
        password_generator = PasswordGeneratorAdapter(
            seed=args["update"]["seed"],
            options=args["update"]["type"]
        )
        password_store = PasswordStoreAdapter()
        command = UpdatePasswordCommand(
            username=args["update"]["username"],
            password_generator=password_generator,
            password_store=password_store
        )
    elif args["get"]["username"] or args["get"]["all"]:
        password_store = PasswordStoreAdapter()
        command = GetPasswordCommand(
            username=args["get"]["username"],
            all_option=args["get"]["all"],
            password_store=password_store
        )
    elif args["upload"]:
        file_uploader = DriveUploaderAdapter()
        command = UploadCommand(file_uploader)
    else:
        print("Unknown action. Use -help to see the list of available commands.")
        return

    command.execute()

if __name__ == "__main__":
    main()

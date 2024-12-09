from application.input_handlers.argument_handler import ArgumentHandler
from application.commands.help_command import HelpCommand
from application.commands.new_password_command import NewPasswordCommand
from application.commands.update_password_command import UpdatePasswordCommand
from application.commands.get_password_command import GetPasswordCommand
from application.commands.upload_command import UploadCommand
from application.commands.delete_password_command import DeletePasswordCommand
from infrastructure.adapters.password_generator_adapter import PasswordGeneratorAdapter
from infrastructure.adapters.password_store_adapter import PasswordStoreAdapter
from infrastructure.adapters.drive_uploader_adapter import DriveUploaderAdapter

def main():
    args = ArgumentHandler().handle_arguments()

    # Check for errors
    if args.error:
        print(f"Error: {args.error}")
        return

    command = None

    # Determine which command to execute
    if args.help:
        command = HelpCommand()
    elif args.new.get("username"):
        password_generator = PasswordGeneratorAdapter(
            seed=args.new.get("seed"),
            options=args.new.get("type")
        )
        password_store = PasswordStoreAdapter()
        command = NewPasswordCommand(
            username=args.new.get("username"),
            domain=args.new.get("domain"),
            password_generator=password_generator,
            password_store=password_store,
            password=args.new.get("password")   
        )
    elif args.update.get("username"):
        password_generator = PasswordGeneratorAdapter(
            seed=args.update.get("seed"),
            options=args.update.get("type")
        )
        password_store = PasswordStoreAdapter()
        command = UpdatePasswordCommand(
            username=args.update.get("username"),
            domain=args.update.get("domain"),
            password_generator=password_generator,
            password_store=password_store
        )
    elif args.get.get("username") or args.get.get("all"):
        password_store = PasswordStoreAdapter()
        command = GetPasswordCommand(
            username=args.get.get("username"),
            domain=args.get.get("domain"),
            all_option=args.get.get("all"),
            password_store=password_store
        )
    elif args.upload:
        file_uploader = DriveUploaderAdapter()
        command = UploadCommand(file_uploader)
    elif args.delete:
        password_store = PasswordStoreAdapter()
        command = DeletePasswordCommand(
            username=args.delete.get("username"),
            domain=args.delete.get("domain"),
            password_store=password_store
        )
    else:
        print("Unknown action. Use -help to see the list of available commands.")
        return

    # Execute the selected command
    command.execute()

if __name__ == "__main__":
    main()
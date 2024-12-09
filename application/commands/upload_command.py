from .base_command import BaseCommand
import dotenv
import os

dotenv.load_dotenv()

class UploadCommand(BaseCommand):
    def __init__(self, file_uploader):
        self.file_uploader = file_uploader

    def execute(self):
        print("Uploading passwords to Google Drive.")
        try:
            password_file_path = os.getenv("PATH_TO_PASSWORD_FILE")
            password_file_name = os.getenv("PASSWORD_FILE_NAME")
            file_to_upload = f"{password_file_path}/{password_file_name}"
            self.file_uploader.upload_file(file_to_upload, "password_manager")
            print("Passwords uploaded successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

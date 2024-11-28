from .base_command import BaseCommand

class UploadCommand(BaseCommand):
    def __init__(self, file_uploader):
        self.file_uploader = file_uploader

    def execute(self):
        print("Uploading passwords to Google Drive.")
        try:
            self.file_uploader.upload_file("passwords.txt", "pass_gen")
            print("Passwords uploaded successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

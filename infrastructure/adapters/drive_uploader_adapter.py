from domain.ports.file_uploader_port import FileUploaderPort
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import dotenv


class DriveUploaderAdapter(FileUploaderPort):
    def __init__(self):
        dotenv.load_dotenv()
        
        self.gauth = GoogleAuth()
        
        self.client_secret_path = os.getenv("PATH_TO_CLIENT_SECRET")
        self.client_secret_namefile = os.getenv("CLIENT_SECRET_NAMEFILE")
        self.password_file_name = os.getenv("PASSWORD_FILE_NAME")

        if not self.client_secret_path or not self.client_secret_namefile:
            raise ValueError("Environment variables for client_secret file path and name are not set.")

        # Construct the full path to the client secret file
        self.client_secret_file_path = os.path.join(self.client_secret_path, self.client_secret_namefile)
        
        # Construct the full path to the password file
        self.password_file_path = os.path.join(self.client_secret_path, self.password_file_name)
        
        if not os.path.exists(self.client_secret_file_path):
            raise FileNotFoundError(
                f"'{self.client_secret_file_path}' not found in {os.getcwd()}.")

        self.gauth.LoadClientConfigFile(self.client_secret_file_path)
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, drive_foldel_name):
        # Define the name of the file we intend to upload
        file_name = self.password_file_name
        
        # Search for the folder on Google Drive
        folder_query = f"title='{drive_foldel_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        folder_list = self.drive.ListFile({'q': folder_query}).GetList()

        if folder_list:
            folder_id = folder_list[0]['id']
        else:
            folder_metadata = {
                'title': drive_foldel_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = self.drive.CreateFile(folder_metadata)
            folder.Upload()
            folder_id = folder['id']

        # Check if the file already exists in the target folder
        file_query = f"title='{file_name}' and '{folder_id}' in parents and trashed=false"
        existing_files = self.drive.ListFile({'q': file_query}).GetList()

        if existing_files:
            existing_file = existing_files[0]
            existing_file.Delete()
            print(f"Existing file '{file_name}' deleted from folder '{drive_foldel_name}'.")

        # Upload the new file to the folder
        file_metadata = {
            'title': file_name,
            'parents': [{'id': folder_id}]
        }
        file = self.drive.CreateFile(file_metadata)
        file.SetContentFile(self.password_file_path)
        file.Upload()
        print(f"File '{file_name}' successfully uploaded to folder '{drive_foldel_name}'.")

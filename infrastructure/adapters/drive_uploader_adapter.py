from domain.ports.file_uploader_port import FileUploaderPort
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import dotenv

dotenv.load_dotenv()

class DriveUploaderAdapter(FileUploaderPort):
    def __init__(self):
        self.gauth = GoogleAuth()
        client_secrets_name = os.getenv(
            "CLIENT_SECRET_NAMEFILE", "client_secrets.json")

        if not os.path.exists(client_secrets_name):
            raise FileNotFoundError(
                f"'{client_secrets_name}' not found in {os.getcwd()}.")

        self.gauth.LoadClientConfigFile(client_secrets_name)
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, file_path, folder_name):
        folder_query = f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        folder_list = self.drive.ListFile({'q': folder_query}).GetList()

        if folder_list:
            folder_id = folder_list[0]['id']
        else:
            folder_metadata = {
                'title': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = self.drive.CreateFile(folder_metadata)
            folder.Upload()
            folder_id = folder['id']

        file_name = os.path.basename(file_path)
        file_query = f"title='{file_name}' and '{folder_id}' in parents and trashed=false"
        existing_files = self.drive.ListFile({'q': file_query}).GetList()

        if existing_files:
            existing_file = existing_files[0]
            existing_file.Delete()
            print(
                f"Existing file '{file_name}' deleted from folder '{folder_name}'.")

        file_metadata = {
            'title': file_name,
            'parents': [{'id': folder_id}]
        }
        file = self.drive.CreateFile(file_metadata)
        file.SetContentFile(file_path)
        file.Upload()
        print(
            f"File '{file_name}' successfully uploaded to folder '{folder_name}'.")

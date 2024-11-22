from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()


class DriveUpload:
    def __init__(self):
        # Authenticate with Google Drive
        self.gauth = GoogleAuth()

        # Get the client secrets file name from the environment variable
        client_secrets_name = os.getenv("CLIENT_SECRET_NAMEFILE", "client_secrets.json")
        
        # Check if the file exists
        if not os.path.exists(client_secrets_name):
            raise FileNotFoundError(f"'{client_secrets_name}' not found in {os.getcwd()}.")

        # Load the client secrets file
        self.gauth.LoadClientConfigFile(client_secrets_name)
        self.gauth.LocalWebserverAuth()  # Opens a local webserver for OAuth2 authentication
        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, file_path, folder_name):
        """
        Uploads a file to a specified folder in Google Drive.
        If the folder doesn't exist, it creates the folder.
        """
        # Check if the specified folder exists on Google Drive
        folder_query = f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        folder_list = self.drive.ListFile({'q': folder_query}).GetList()

        if folder_list:
            folder_id = folder_list[0]['id']  # Use existing folder's ID
        else:
            # Create the folder if it doesn't exist
            folder_metadata = {
                'title': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = self.drive.CreateFile(folder_metadata)
            folder.Upload()
            folder_id = folder['id']

        # Upload the file to the specified folder
        file_metadata = {
            'title': os.path.basename(file_path),
            'parents': [{'id': folder_id}]
        }
        file = self.drive.CreateFile(file_metadata)
        file.SetContentFile(file_path)  # Set the file content
        file.Upload()
        print(f"File '{file_path}' successfully uploaded to folder '{folder_name}'.")


if __name__ == "__main__":
    # Specify the file and folder to upload
    file_to_upload = "passwords.txt"
    folder_name = "pass_gen"

    # Ensure the file exists before attempting to upload
    if os.path.exists(file_to_upload):
        uploader = DriveUpload()
        uploader.upload_file(file_to_upload, folder_name)
    else:
        print(f"File '{file_to_upload}' does not exist.")

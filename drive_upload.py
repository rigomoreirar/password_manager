from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import dotenv

# Load environment variables
dotenv.load_dotenv()


class DriveUpload:
    def __init__(self):
        """
        Initializes Google Drive authentication.
        Loads the client secrets file specified in the environment variable.
        Performs OAuth2 authentication using a local web server.
        """
        self.gauth = GoogleAuth()

        # Get the client secrets file name from the environment variable
        client_secrets_name = os.getenv(
            "CLIENT_SECRET_NAMEFILE", "client_secrets.json")

        # Check if the client secrets file exists
        if not os.path.exists(client_secrets_name):
            raise FileNotFoundError(f"'{client_secrets_name}' not found in {os.getcwd()}.")

        # Load the client secrets file
        self.gauth.LoadClientConfigFile(client_secrets_name)
        # Opens a local web server for OAuth2 authentication
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, file_path, folder_name):
        """
        Uploads a file to a specified folder in Google Drive.
        If the folder doesn't exist, it creates the folder.
        If a file with the same name exists in the folder, it deletes the old file and uploads the new one.

        Args:
            file_path (str): The path to the file to upload.
            folder_name (str): The name of the folder to upload the file to.
        """
        # Query to check if the specified folder exists on Google Drive
        folder_query = f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        folder_list = self.drive.ListFile({'q': folder_query}).GetList()

        # Get the folder ID or create the folder if it doesn't exist
        if folder_list:
            # Use the ID of the existing folder
            folder_id = folder_list[0]['id']
        else:
            folder_metadata = {
                'title': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = self.drive.CreateFile(folder_metadata)
            folder.Upload()
            folder_id = folder['id']

        # Check if a file with the same name exists in the target folder
        file_name = os.path.basename(file_path)
        file_query = f"title='{file_name}' and '{folder_id}' in parents and trashed=false"
        existing_files = self.drive.ListFile({'q': file_query}).GetList()

        # If a file exists, delete it before uploading the new file
        if existing_files:
            existing_file = existing_files[0]
            existing_file.Delete()
            print(f"Existing file '{file_name}' deleted from folder '{folder_name}'.")

        # Upload the new file to the specified folder
        file_metadata = {
            'title': file_name,
            'parents': [{'id': folder_id}]
        }
        file = self.drive.CreateFile(file_metadata)
        file.SetContentFile(file_path)  # Set the file content
        file.Upload()
        print(f"File '{file_name}' successfully uploaded to folder '{folder_name}'.")


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

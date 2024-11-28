import unittest
from unittest.mock import patch, MagicMock
from infrastructure.adapters.drive_uploader_adapter import DriveUploaderAdapter

class TestDriveUploaderAdapter(unittest.TestCase):
    @patch('infrastructure.adapters.drive_uploader_adapter.GoogleAuth')
    @patch('infrastructure.adapters.drive_uploader_adapter.GoogleDrive')
    def test_upload_file(self, mock_drive_class, mock_auth_class):
        # Mock the authentication
        mock_auth_instance = MagicMock()
        mock_auth_class.return_value = mock_auth_instance

        # Mock the Google Drive instance
        mock_drive_instance = MagicMock()
        mock_drive_class.return_value = mock_drive_instance

        # Mock the methods used in upload_file
        mock_file = MagicMock()
        mock_drive_instance.CreateFile.return_value = mock_file

        adapter = DriveUploaderAdapter()
        adapter.upload_file('test_file.txt', 'test_folder')

        # Assertions
        mock_auth_class.assert_called_once()
        mock_drive_class.assert_called_once_with(mock_auth_instance)
        mock_drive_instance.CreateFile.assert_called()
        mock_file.SetContentFile.assert_called_with('test_file.txt')
        mock_file.Upload.assert_called_once()

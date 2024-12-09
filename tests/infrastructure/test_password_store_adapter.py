import unittest
from unittest.mock import mock_open, patch
from infrastructure.adapters.password_store_adapter import PasswordStoreAdapter
from domain.ports.password_store_port import PasswordStorePort
from domain.models.password_entry_model import PasswordEntryModel
import os
import dotenv

class PasswordStoreAdapter(PasswordStorePort):
    def __init__(self):
        dotenv.load_dotenv()  

        password_file_path = os.getenv("PATH_TO_PASSWORD_FILE")
        password_file_name = os.getenv("PASSWORD_FILE_NAME")
        if not password_file_path or not password_file_name:
            raise ValueError("Environment variables for password file path and name are not set.")

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='user1|pass1|domain1\nuser2|pass2|domain2\n')
    def test_get_password(self, mock_file, mock_exists):
        mock_exists.return_value = True  # Simulate that the password file exists
        password = self.adapter.get_password('user1', 'domain1')
        self.assertEqual(password, 'pass1')
        mock_file.assert_called_with('./passwords.txt', 'r')

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_add_password(self, mock_file, mock_exists):
        mock_exists.return_value = True  # Simulate that the password file exists
        # Mock reading existing entries
        mock_file.return_value.__enter__.return_value.readlines.return_value = [
            'user1|pass1|domain1\n',
            'user2|pass2|domain2\n'
        ]
        entry = PasswordEntryModel(username='user3', password='pass3', domain='domain3')
        self.adapter.add_password(entry)
        # Check that the file was opened in append mode
        mock_file.assert_any_call('./passwords.txt', 'a')
        # Check that the new entry was written
        handle = mock_file()
        handle.write.assert_called_once_with('user3|pass3|domain3\n')

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_update_password(self, mock_file, mock_exists):
        mock_exists.return_value = True  # Simulate that the password file exists
        # Mock reading existing entries
        mock_file.return_value.__enter__.return_value.readlines.return_value = [
            'user1|pass1|domain1\n',
            'user2|pass2|domain2\n'
        ]
        entry = PasswordEntryModel(username='user1', password='newpass', domain='domain1')
        self.adapter.update_password(entry)
        # Check that the file was opened correctly
        mock_file.assert_any_call('./passwords.txt', 'w')
        # Check that the updated entries were written
        handle = mock_file()
        expected_calls = [
            unittest.mock.call('user1|newpass|domain1\n'),
            unittest.mock.call('user2|pass2|domain2\n')
        ]
        handle.write.assert_has_calls(expected_calls, any_order=False)

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_delete_password(self, mock_file, mock_exists):
        mock_exists.return_value = True  # Simulate that the password file exists
        # Mock reading existing entries
        mock_file.return_value.__enter__.return_value.readlines.return_value = [
            'user1|pass1|domain1\n',
            'user2|pass2|domain2\n'
        ]
        entry = PasswordEntryModel(username='user1', password='', domain='domain1')
        self.adapter.delete_password(entry)
        # Check that the file was opened correctly
        mock_file.assert_any_call('./passwords.txt', 'w')
        # Check that the remaining entries were written
        handle = mock_file()
        handle.write.assert_called_once_with('user2|pass2|domain2\n')

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_all_usernames(self, mock_file, mock_exists):
        mock_exists.return_value = True  # Simulate that the password file exists
        read_data = 'user1|pass1|domain1\nuser2|pass2|domain2\nuser1|pass3|domain3\n'
        mock_file.return_value.__enter__.return_value.readlines.return_value = read_data.strip().split('\n')
        usernames = self.adapter.get_all_usernames()
        expected_usernames = [('user1', 'domain1'), ('user2', 'domain2'), ('user1', 'domain3')]
        self.assertEqual(sorted(usernames), sorted(expected_usernames))
        mock_file.assert_called_with('./passwords.txt', 'r')

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_get_all_passwords(self, mock_file, mock_exists):
        mock_exists.return_value = True  # Simulate that the password file exists
        read_data = 'user1|pass1|domain1\nuser2|pass2|domain2\n'
        mock_file.return_value.__enter__.return_value.readlines.return_value = read_data.strip().split('\n')
        passwords = self.adapter.get_all_passwords()
        expected_passwords = [
            {"username": "user1", "password": "pass1", "domain": "domain1"},
            {"username": "user2", "password": "pass2", "domain": "domain2"}
        ]
        self.assertEqual(passwords, expected_passwords)
        mock_file.assert_called_with('./passwords.txt', 'r')

if __name__ == '__main__':
    unittest.main()
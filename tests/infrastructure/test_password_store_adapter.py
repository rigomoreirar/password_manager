import unittest
from unittest.mock import mock_open, patch
from infrastructure.adapters.password_store_adapter import PasswordStoreAdapter
from domain.models.password_entry_model import PasswordEntryModel

class TestPasswordStoreAdapter(unittest.TestCase):
    def setUp(self):
        self.adapter = PasswordStoreAdapter(file_path='passwords.txt')

    @patch('builtins.open', new_callable=mock_open, read_data='user1|pass1\nuser2|pass2\n')
    def test_get_password(self, mock_file):
        password = self.adapter.get_password('user1')
        self.assertEqual(password, 'pass1')
        mock_file.assert_called_with('passwords.txt', 'r')

    @patch('builtins.open', new_callable=mock_open)
    def test_add_password(self, mock_file):
        entry = PasswordEntryModel(username='user3', password='pass3')
        self.adapter.add_password(entry)
        mock_file.assert_called_with('passwords.txt', 'a')
        handle = mock_file()
        handle.write.assert_called_once_with('user3|pass3\n')

    @patch('builtins.open', new_callable=mock_open, read_data='user1|pass1\nuser2|pass2\n')
    def test_update_password(self, mock_file):
        # Mock the read and write operations
        handle = mock_file()
        handle.readlines.return_value = ['user1|pass1\n', 'user2|pass2\n']
        entry = PasswordEntryModel(username='user1', password='newpass')
        self.adapter.update_password(entry)
        mock_file.assert_called_with('passwords.txt', 'w')
        handle.write.assert_any_call('user1|newpass\n')
        handle.write.assert_any_call('user2|pass2\n')

if __name__ == '__main__':
    unittest.main()

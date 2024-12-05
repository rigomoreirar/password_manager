import unittest
from unittest.mock import MagicMock, patch
from application.commands.update_password_command import UpdatePasswordCommand
from domain.services.password_service import PasswordService
from domain.models.password_entry_model import PasswordEntryModel

class TestUpdatePasswordCommand(unittest.TestCase):
    def setUp(self):
        # Mock the password generator and store
        self.mock_password_generator = MagicMock()
        self.mock_password_store = MagicMock()
        
        # Patch the PasswordService to use the mocks
        self.password_service_patch = patch('application.commands.update_password_command.PasswordService')
        self.mock_password_service_class = self.password_service_patch.start()
        self.mock_password_service = MagicMock(spec=PasswordService)
        self.mock_password_service_class.return_value = self.mock_password_service
        
        # Instantiate the command
        self.command = UpdatePasswordCommand(
            username='test_user',
            domain='test_domain',  # Added 'domain' parameter
            password_generator=self.mock_password_generator,
            password_store=self.mock_password_store
        )

    def tearDown(self):
        self.password_service_patch.stop()

    def test_execute_success(self):
        # Setup the mock password service
        self.mock_password_service.update_password.return_value = PasswordEntryModel(
            'test_user', 'updated_password', 'test_domain'
        )
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.update_password.assert_called_once_with('test_user', 'test_domain')
        mock_print.assert_any_call("Updating password for username: test_user. In domain: test_domain.")
        mock_print.assert_any_call(
            "Generated updated password: PasswordEntryModel(username='test_user', password='updated_password', domain='test_domain')"
        )
        mock_print.assert_any_call("Password updated successfully for username: test_user.")

    def test_execute_exception(self):
        # Setup the mock password service to raise an exception
        self.mock_password_service.update_password.side_effect = Exception('Test exception')
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.update_password.assert_called_once_with('test_user', 'test_domain')
        mock_print.assert_any_call("Updating password for username: test_user. In domain: test_domain.")
        mock_print.assert_any_call("An error occurred: Test exception")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import MagicMock, patch
from application.commands.new_password_command import NewPasswordCommand
from domain.services.password_service import PasswordService
from domain.models.password_entry_model import PasswordEntryModel


class TestNewPasswordCommand(unittest.TestCase):
    def setUp(self):
        # Mock the password generator and store
        self.mock_password_generator = MagicMock()
        self.mock_password_store = MagicMock()
        
        # Patch the PasswordService to use the mocks
        patcher = patch('application.commands.new_password_command.PasswordService')
        self.mock_password_service_class = patcher.start()
        self.addCleanup(patcher.stop)
        
        self.mock_password_service = MagicMock(spec=PasswordService)
        self.mock_password_service_class.return_value = self.mock_password_service
        
        # Instantiate the command
        self.command = NewPasswordCommand(
            username='test_user',
            domain='test_domain',
            password_generator=self.mock_password_generator,
            password_store=self.mock_password_store,
            password='existing_password'  
        )

    def tearDown(self):
        # This is handled by addCleanup in setUp, so it's optional
        pass

    def test_execute_success_with_existing_password(self):
        # Setup the mock password service
        password_entry = PasswordEntryModel(username='test_user', password='existing_password', domain='test_domain')
        self.mock_password_service.add_existing_password.return_value = password_entry
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.add_existing_password.assert_called_once()
        args, kwargs = self.mock_password_service.add_existing_password.call_args
        self.assertEqual(args[0].username, 'test_user')
        self.assertEqual(args[0].password, 'existing_password')
        self.assertEqual(args[0].domain, 'test_domain')
        
        mock_print.assert_any_call("Creating a new password for username: test_user. In domain: test_domain.")
        mock_print.assert_any_call(f"Added existing password: {password_entry}")
        mock_print.assert_any_call("Password stored successfully for username: test_user.")

    def test_execute_success_with_generated_password(self):
        # Setup the command without existing password
        self.command.password = None
        generated_password_entry = PasswordEntryModel(username='test_user', password='mocked_password', domain='test_domain')
        self.mock_password_service.create_password.return_value = generated_password_entry
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.create_password.assert_called_once_with('test_user', 'test_domain')
        mock_print.assert_any_call("Creating a new password for username: test_user. In domain: test_domain.")
        mock_print.assert_any_call(f"Generated password: {generated_password_entry}")
        mock_print.assert_any_call("Password stored successfully for username: test_user.")

    def test_execute_exception(self):
        # Set password to None to force the use of create_password()
        self.command.password = None
    
        # Setup the mock password service to raise an exception
        self.mock_password_service.create_password.side_effect = Exception('Test exception')
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.create_password.assert_called_once_with('test_user', 'test_domain')
        mock_print.assert_any_call("Creating a new password for username: test_user. In domain: test_domain.")
        mock_print.assert_any_call("An error occurred: Test exception")

if __name__ == '__main__':
    unittest.main()
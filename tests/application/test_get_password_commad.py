import unittest
from unittest.mock import MagicMock, patch
from application.commands.get_password_command import GetPasswordCommand
from domain.services.password_service import PasswordService

class TestGetPasswordCommand(unittest.TestCase):
    def setUp(self):
        # Mock the password store
        self.mock_password_store = MagicMock()
        
        # Patch the PasswordService to use the mocks
        self.password_service_patch = patch('application.commands.get_password_command.PasswordService')
        self.mock_password_service_class = self.password_service_patch.start()
        self.mock_password_service = MagicMock(spec=PasswordService)
        self.mock_password_service_class.return_value = self.mock_password_service
        
        # Instantiate the command
        self.command = GetPasswordCommand(
            username='test_user',
            domain='test_domain',
            all_option=None,
            password_store=self.mock_password_store
        )

    def tearDown(self):
        self.password_service_patch.stop()

    def test_execute_retrieve_password(self):
        # Setup the mock password service
        self.mock_password_service.retrieve_password.return_value = 'mocked_password'
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.retrieve_password.assert_called_once_with('test_user', 'test_domain')
        mock_print.assert_any_call("Retrieving password for username: test_user. In domain: test_domain.")
        mock_print.assert_any_call("Password for username 'test_user': mocked_password")

    def test_execute_retrieve_all_usernames(self):
        # Setup the command to retrieve all usernames
        self.command.username = None
        self.command.all_option = "usernames"
        self.mock_password_service.retrieve_all_usernames.return_value = ['user1', 'user2']
        
        # Capture the output
        with patch('builtins.print') as mock_print, patch('pprint.pprint') as mock_pprint:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.retrieve_all_usernames.assert_called_once()
        mock_print.assert_any_call("Retrieving all usernames.")
        mock_pprint.assert_any_call({"All Usernames": ['user1', 'user2']})

    def test_execute_retrieve_all_passwords(self):
        # Setup the command to retrieve all passwords
        self.command.username = None
        self.command.all_option = "passwords"
        self.mock_password_service.retrieve_all_passwords.return_value = [
            {"username": "user1", "password": "pass1", "domain": "domain1"},
            {"username": "user2", "password": "pass2", "domain": "domain2"}
        ]
        
        # Capture the output
        with patch('builtins.print') as mock_print, patch('pprint.pprint') as mock_pprint:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.retrieve_all_passwords.assert_called_once()
        mock_print.assert_any_call("Retrieving all passwords.")
        mock_pprint.assert_any_call({"All Passwords": [
            {"username": "user1", "password": "pass1", "domain": "domain1"},
            {"username": "user2", "password": "pass2", "domain": "domain2"}
        ]})

    def test_execute_retrieve_all_in_domain(self):
        # Setup the command to retrieve all usernames and passwords in a domain
        self.command.username = None
        self.command.all_option = "domain"
        self.mock_password_service.retrieve_all_in_domain.return_value = [
            {"username": "user1", "password": "pass1"},
            {"username": "user2", "password": "pass2"}
        ]
        
        # Capture the output
        with patch('builtins.print') as mock_print, patch('pprint.pprint') as mock_pprint:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.retrieve_all_in_domain.assert_called_once_with('test_domain')
        mock_print.assert_any_call("Retrieving all usernames and passwords in domain: test_domain.")
        mock_pprint.assert_any_call({"All Usernames and passwords in Domain": [
            {"username": "user1", "password": "pass1"},
            {"username": "user2", "password": "pass2"}
        ]})

    def test_execute_invalid_command(self):
        # Setup the command with invalid options
        self.command.username = None
        self.command.all_option = None
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        mock_print.assert_any_call("Invalid get command.")

    def test_execute_exception(self):
        # Setup the mock password service to raise an exception
        self.mock_password_service.retrieve_password.side_effect = Exception('Test exception')
        
        # Capture the output
        with patch('builtins.print') as mock_print:
            self.command.execute()
        
        # Assertions
        self.mock_password_service.retrieve_password.assert_called_once_with('test_user', 'test_domain')
        mock_print.assert_any_call("Retrieving password for username: test_user. In domain: test_domain.")
        mock_print.assert_any_call("An error occurred: Test exception")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import MagicMock
from domain.services.password_service import PasswordService
from domain.ports.password_store_port import PasswordStorePort
from domain.ports.password_generator_port import PasswordGeneratorPort
from domain.models.password_entry import PasswordEntry

class TestPasswordService(unittest.TestCase):
    def setUp(self):
        # Create mock instances of the ports
        self.mock_password_store = MagicMock(spec=PasswordStorePort)
        self.mock_password_generator = MagicMock(spec=PasswordGeneratorPort)
        
        # Instantiate the service with the mock ports
        self.service = PasswordService(
            password_store=self.mock_password_store,
            password_generator=self.mock_password_generator
        )

    def test_create_password(self):
        # Setup the mock password generator to return a specific password
        self.mock_password_generator.generate_password.return_value = 'mocked_password'
        
        # Call the method under test
        result = self.service.create_password('test_user')
        
        # Assertions
        self.assertIsInstance(result, PasswordEntry)
        self.assertEqual(result.username, 'test_user')
        self.assertEqual(result.password, 'mocked_password')
        self.mock_password_generator.generate_password.assert_called_once()
        self.mock_password_store.add_password.assert_called_once_with(result)

    def test_update_password(self):
        # Setup the mock password generator to return a specific password
        self.mock_password_generator.generate_password.return_value = 'updated_password'
        
        # Call the method under test
        result = self.service.update_password('test_user')
        
        # Assertions
        self.assertIsInstance(result, PasswordEntry)
        self.assertEqual(result.username, 'test_user')
        self.assertEqual(result.password, 'updated_password')
        self.mock_password_generator.generate_password.assert_called_once()
        self.mock_password_store.update_password.assert_called_once_with(result)

    def test_retrieve_password(self):
        # Setup the mock password store to return a specific password
        self.mock_password_store.get_password.return_value = 'existing_password'
        
        # Call the method under test
        result = self.service.retrieve_password('test_user')
        
        # Assertions
        self.assertEqual(result, 'existing_password')
        self.mock_password_store.get_password.assert_called_once_with('test_user')

    def test_retrieve_all_usernames(self):
        # Setup the mock password store to return a list of usernames
        self.mock_password_store.get_all_usernames.return_value = ['user1', 'user2']
        
        # Call the method under test
        result = self.service.retrieve_all_usernames()
        
        # Assertions
        self.assertEqual(result, ['user1', 'user2'])
        self.mock_password_store.get_all_usernames.assert_called_once()

    def test_retrieve_all_passwords(self):
        # Setup the mock password store to return a list of passwords
        self.mock_password_store.get_all_passwords.return_value = [
            {'username': 'user1', 'password': 'pass1'},
            {'username': 'user2', 'password': 'pass2'}
        ]
        
        # Call the method under test
        result = self.service.retrieve_all_passwords()
        
        # Assertions
        self.assertEqual(result, [
            {'username': 'user1', 'password': 'pass1'},
            {'username': 'user2', 'password': 'pass2'}
        ])
        self.mock_password_store.get_all_passwords.assert_called_once()

if __name__ == '__main__':
    unittest.main()

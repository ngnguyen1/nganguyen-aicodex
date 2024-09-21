import unittest
from unittest.mock import patch, MagicMock
from users.repositories import UserRepository
from users.services import UserService
from users.models import User
from extensions import db
from flask import Flask

class TestUserRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config.from_object('config_test')
        db.init_app(cls.app)
        cls.app.app_context().push()

    @patch('users.repositories.User.query')
    def test_get_all(self, mock_query):
        mock_query.all.return_value = ['user1', 'user2']
        result = UserRepository.get_all()
        self.assertEqual(result, ['user1', 'user2'])
        mock_query.all.assert_called_once()

    @patch('users.repositories.User.query')
    def test_get_by_id(self, mock_query):
        mock_user = MagicMock()
        mock_query.get.return_value = mock_user
        result = UserRepository.get_by_id(1)
        self.assertEqual(result, mock_user)
        mock_query.get.assert_called_once_with(1)

    @patch('users.repositories.db.session')
    def test_create(self, mock_session):
        mock_user = MagicMock()
        UserRepository.create(mock_user)
        mock_session.add.assert_called_once_with(mock_user)
        mock_session.commit.assert_called_once()

    @patch('users.repositories.db.session')
    def test_update(self, mock_session):
        UserRepository.update()
        mock_session.commit.assert_called_once()

    @patch('users.repositories.db.session')
    def test_delete(self, mock_session):
        mock_user = MagicMock()
        UserRepository.delete(mock_user)
        mock_session.delete.assert_called_once_with(mock_user)
        mock_session.commit.assert_called_once()

    @patch('users.repositories.User.query')
    def test_get_by_email(self, mock_query):
        mock_user = MagicMock()
        mock_query.filter_by.return_value.first.return_value = mock_user
        result = UserRepository.get_by_email('test@example.com')
        self.assertEqual(result, mock_user)
        mock_query.filter_by.assert_called_once_with(email='test@example.com')
        mock_query.filter_by.return_value.first.assert_called_once()

class TestUserService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config.from_object('config_test')
        db.init_app(cls.app)
        cls.app.app_context().push()

    @patch('users.repositories.UserRepository.get_by_email')
    def test_get_user_by_email(self, mock_get_by_email):
        # Mock a user object
        mock_user = MagicMock()
        mock_user.email = 'test@example.com'
        mock_get_by_email.return_value = mock_user

        # Test with a valid email
        result = UserService.get_user_by_email('test@example.com')
        self.assertEqual(result, mock_user)
        mock_get_by_email.assert_called_once_with('test@example.com')

        # Test with an invalid email
        result = UserService.get_user_by_email('invalid-email')
        self.assertFalse(result)

        # Test with a non-existing email
        mock_get_by_email.return_value = None
        result = UserService.get_user_by_email('nonexistent@example.com')
        self.assertFalse(result)
        mock_get_by_email.assert_called_with('nonexistent@example.com')

if __name__ == '__main__':
    unittest.main()
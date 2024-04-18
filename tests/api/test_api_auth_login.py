from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

UserModel = get_user_model()


class LoginViewTestCase(APITestCase):
    login_url = reverse('api:auth:login')

    def setUp(self):
        self.user = UserModel.objects.create_user(email='test@test.com', password='password')

    def test_login_valid(self):
        """Test if a user is logged in successfully with valid data."""
        login_data = {
            'email': 'test@test.com',
            'password': 'password',
        }

        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if response contains `refresh` and `access`
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def test_login_wrong_email(self):
        """Test if user is not logged if mail is wrong."""
        login_data = {
            'email': 'wrong@email.com',
            'password': 'password',
        }

        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_wrong_password(self):
        """Test if user is not logged if password is wrong."""
        login_data = {
            'email': 'test@test.com',
            'password': 'wrong_password',
        }

        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LoginValidationTestCase(APITestCase):
    login_url = reverse('api:auth:login')

    def test_login_invalid_email(self):
        """Test if a user fails to log in login validation with an invalid email format."""
        login_data = {
            'email': 'Invalid email',
            'password': 'password',
        }

        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_empty_email(self):
        """Test if a user fails to log in validation with an empty email."""
        login_data = {
            'email': '',
            'password': 'password',
        }

        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_empty_password(self):
        """Test if a user fails to log in validation with an empty password."""
        login_data = {
            'email': 'test@test.com',
            'password': '',
        }

        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

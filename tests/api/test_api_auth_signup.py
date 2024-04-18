from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

UserModel = get_user_model()


class SignUpViewTestCase(APITestCase):
    signup_url = reverse('api:auth:signup')

    def test_signup_valid(self):
        """Test if a user is successfully created with valid data."""
        user_data = {
            'email': 'test@test.com',
            'password': 'password',
            'password_confirm': 'password',
            'first_name': 'ABC',
            'last_name': '123',
        }

        response = self.client.post(self.signup_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = UserModel.objects.filter(email=user_data['email']).first()

        self.assertIsNotNone(user, "User was not created")
        self.assertTrue(user.check_password(user_data['password']), "User password does not match given password")
        self.assertEqual(user.first_name, user_data['first_name'], "User first name does not match given first name")
        self.assertEqual(user.last_name, user_data['last_name'], "User last name does not match given last name")

    def test_signup_email_already_exist(self):
        """Test if a user is not created with an email that is already taken."""
        # Create a user with the same email to test
        UserModel.objects.create_user(email='existing@test.com', password='password')

        user_data = {
            'email': 'existing@test.com',  # Invalid email format
            'password': 'password',
            'password_confirm': 'password',
            'first_name': 'ABC',
            'last_name': '123',
        }

        response = self.client.post(self.signup_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        users_count = UserModel.objects.count()
        self.assertEqual(users_count, 1)


class SignUpValidationTestCase(APITestCase):
    signup_url = reverse('api:auth:signup')

    def test_signup_invalid_email(self):
        """Test if a user fails signup validation with an invalid email format."""
        user_data = {
            'email': 'Invalid email',  # Invalid email
            'password': 'password',
            'password_confirm': 'password',
            'first_name': 'ABC',
            'last_name': '123',
        }

        response = self.client.post(self.signup_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        users_count = UserModel.objects.count()
        self.assertEqual(users_count, 0)

    def test_signup_missing_required_fields(self):
        """Test if a user fails signup validation with missing required fields."""
        user_data = {
            'email': 'test@test.com',
            'password': 'password',
            'password_confirm': 'password',
            'last_name': '123',
        }

        response = self.client.post(self.signup_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        users_count = UserModel.objects.count()
        self.assertEqual(users_count, 0)

    def test_signup_passwords_does_not_match(self):
        """Test if a user fails signup validation with passwords not matching."""
        user_data = {
            'email': 'test@test.com',
            'password': 'password',
            'password_confirm': 'wrong_password',
            'first_name': 'ABC',
            'last_name': '123',
        }

        response = self.client.post(self.signup_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        users_count = UserModel.objects.count()
        self.assertEqual(users_count, 0)

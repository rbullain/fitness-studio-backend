from django.test import TestCase
from django.contrib.auth import get_user_model


class UserCreationTestCase(TestCase):
    UserModel = get_user_model()

    def test_create_user(self):
        """Test if a user is created successfully."""
        email = 'user@email.com'
        password = 'foo'

        user_obj = self.UserModel.objects.create_user(email=email, password=password)

        self.assertEqual(user_obj.email, email)
        self.assertTrue(user_obj.check_password(password))
        self.assertTrue(user_obj.is_active)

        self.assertFalse(user_obj.is_staff)

    def test_create_user_with_valid_email_normalizes_email(self):
        """Test if the email is normalized."""
        email = 'USeR@EmAil.COM'

        user_obj = self.UserModel.objects.create_user(email=email, password='foo')

        self.assertEqual(user_obj.email, self.UserModel.objects.normalize_email(email))

    def test_create_superuser(self):
        """Test if the superuser flags are set."""
        user_obj = self.UserModel.objects.create_superuser(email='superuser@email.com', password='foo')

        self.assertTrue(user_obj.is_superuser)
        self.assertTrue(user_obj.is_staff)

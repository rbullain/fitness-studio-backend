from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

UserModel = get_user_model()


class ProfileViewTestCase(APITestCase):
    profile_url = reverse('api:accounts:me')

    def setUp(self):
        self.user = UserModel.objects.create_user(email='test@test.com', password='password')

    def _authenticate_user(self, user):
        """Helper function to authenticate an user. Set the JWT token in the header for the client."""
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def test_user_profile_authenticated(self):
        """Test access to the user profile with authentication."""
        self.client.login(email='test@test.com', password='password')

        self._authenticate_user(self.user)

        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_profile_unauthenticated(self):
        """Test access to the user profile without authentication."""
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

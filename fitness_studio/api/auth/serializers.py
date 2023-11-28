from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenBlacklistSerializer

UserModel = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    """Serializer for user signup."""
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ('email', 'password', 'password_confirm', 'first_name', 'last_name',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password_confirm': "Passwords did not match"})
        return attrs

    def create(self, validated_data):
        user_data = {
            'email': validated_data['email'],
            'password': validated_data['password'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
        }

        user = UserModel.objects.create_user(**user_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    """Serializer for user login."""


class LogoutSerializer(TokenBlacklistSerializer):
    """Serializer for user logout."""

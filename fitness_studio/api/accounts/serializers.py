from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    """"""
    bio = serializers.CharField(source='profile.bio')
    birth_date = serializers.DateField(source='profile.birth_date')
    gender = serializers.CharField(source='profile.gender')
    picture = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'bio', 'birth_date', 'gender', 'picture',)
        extra_kwargs = {
            'email': {'read_only': True},
        }

    def get_picture(self, obj):
        profile = obj.profile
        if profile is None:
            return None

        if profile.picture:
            return profile.picture.url
        return None

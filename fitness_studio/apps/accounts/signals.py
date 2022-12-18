from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from apps.accounts.models import UserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def on_user_creation_create_profile(instance: UserModel, created, **kwargs):
    """Create a UserProfile related to the new user on creation."""
    if created:
        if not hasattr(instance, 'profile'):
            profile = UserProfile.objects.create(user=instance)

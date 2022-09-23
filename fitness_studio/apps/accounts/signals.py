from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from apps.accounts.models import UserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def on_user_update(instance: UserModel, created, **kwargs):
    if created:
        if not hasattr(instance, 'profile'):
            profile = UserProfile.objects.create(user=instance)

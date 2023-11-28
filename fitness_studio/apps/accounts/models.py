from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField, PPOIField
from django_extensions.db.models import TimeStampedModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_staff=False, is_active=True, **extra_fields):
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=is_active, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    """Custom User model with email field as username."""
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('first name'), max_length=40)
    last_name = models.CharField(_('last name'), max_length=40)

    is_staff = models.BooleanField(_('is staff'), default=False)
    is_active = models.BooleanField(_('is active'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('-created', '-modified',)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_full_name_prettier(self):
        full_name = f"{self.first_name.title()} {self.last_name.upper()}"
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.email


class UserProfile(models.Model):
    """User profile information."""

    class Gender(models.TextChoices):
        MALE = ("M", _("Male"))
        FEMALE = ("F", _("Female"))
        OTHER = ("O", _("Other"))
        __empty__ = _("Not specified")

    MAX_BIO_LENGTH = 255

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
        verbose_name=_('user'))
    bio = models.TextField(_('bio'), max_length=MAX_BIO_LENGTH, blank=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    gender = models.CharField(_('gender'), max_length=1, choices=Gender.choices, null=True, blank=True)

    picture = VersatileImageField(_('picture'), upload_to='images/profiles/', ppoi_field='ppoi', null=True,
        blank=True)
    ppoi = PPOIField(_('picture PPOI'))

    class Meta:
        verbose_name = _('user profile')

    def __str__(self):
        return self.user.get_username()

"""
Use this file as a basis for setting up your project configuration, and do not
forget about changing in the __init__.py file the right settings to use.

Before deployment: https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
"""
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+eos5=)_n0y#_v15&8cj#g)fdf^m7)!ibr@)d)0&wir9s53tof'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Auth
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 0,
        }
    },
]

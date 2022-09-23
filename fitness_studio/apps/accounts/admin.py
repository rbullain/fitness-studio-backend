from django.contrib import admin

from apps.accounts.models import User, UserProfile


@admin.register(User, UserProfile)
class UserAdmin(admin.ModelAdmin):
    pass

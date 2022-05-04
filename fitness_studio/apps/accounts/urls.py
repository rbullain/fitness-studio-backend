from django.urls import path

from apps.accounts.views import UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
]

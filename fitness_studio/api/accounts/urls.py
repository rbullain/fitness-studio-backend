from django.urls import path

from api.accounts.views import UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('me', UserProfileView.as_view(), name='me'),
]

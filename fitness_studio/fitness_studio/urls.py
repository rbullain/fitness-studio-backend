from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LogoutView

from apps.accounts.views import UserSignUpView, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    # Auth
    path('accounts/sign-up/', UserSignUpView.as_view(), name='account_signup'),
    path('accounts/login/', UserLoginView.as_view(), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),

    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('classes/', include('apps.classes.urls', namespace='classes')),
]

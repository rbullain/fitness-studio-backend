from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView, LogoutView

from apps.accounts.views import UserSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    # Auth
    path('accounts/sign-up/', UserSignUpView.as_view(), name='account_signup'),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),

    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('classes/', include('apps.classes.urls', namespace='classes')),
]

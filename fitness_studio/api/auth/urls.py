from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from api.auth.views import SignUpView, LoginView

app_name = 'auth'

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token-verify'),
]

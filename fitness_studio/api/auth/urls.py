from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.auth.views import SignUpView

app_name = 'auth'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-get'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),

    path('signup/', SignUpView.as_view(), name='signup'),
]

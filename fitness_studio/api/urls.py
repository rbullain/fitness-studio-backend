from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('auth/', include('api.auth.urls', namespace='auth')),
    path('accounts/', include('api.accounts.urls', namespace='accounts')),
]

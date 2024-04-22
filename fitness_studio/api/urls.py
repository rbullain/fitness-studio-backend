from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('auth/', include('api.auth.urls', namespace='auth')),
    path('accounts/', include('api.accounts.urls', namespace='accounts')),
    path('classes/', include('api.classes.urls', namespace='classes')),
    path('locations/', include('api.locations.urls', namespace='locations')),
]

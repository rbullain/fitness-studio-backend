from django.urls import path, include

urlpatterns = [
    path('classes/', include('api.classes.urls')),
    path('locations/', include('api.locations.urls')),
]

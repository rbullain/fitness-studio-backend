from django.urls import path, include

urlpatterns = [
    path('classes/', include('api.classes.urls')),
]

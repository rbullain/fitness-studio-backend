from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.locations import views

router = DefaultRouter()
router.register('amenities', views.AmenityReadViewSet, basename='amenities')
router.register('locations', views.LocationReadViewSet, basename='locations')

urlpatterns = [
    path('', include(router.urls)),
]

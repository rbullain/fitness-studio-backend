from rest_framework.routers import DefaultRouter

from api.locations import views

router = DefaultRouter()
router.register('locations/amenities', views.AmenityReadViewSet, basename='amenities')
router.register('locations/locations', views.LocationReadViewSet, basename='locations')

from django.urls import path

from api.locations.views import (
    LocationListCreateView,
    AmenitiesListCreateView,
    AddressListCreateView,
)

app_name = 'locations'

urlpatterns = [
    path('amenity', AmenitiesListCreateView.as_view()),
    path('address', AddressListCreateView.as_view()),
    path('location', LocationListCreateView.as_view()),
]

from rest_framework import viewsets

from apps.locations.models import Amenity, Location
from api.locations import serializers


class AmenityReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = serializers.AmenityReadSerializer


class LocationReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationReadSerializer
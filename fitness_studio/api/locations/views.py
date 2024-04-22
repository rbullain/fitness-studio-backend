from rest_framework.generics import ListCreateAPIView

from apps.locations.models import Location, Address, Amenity
from api.locations.serializers import LocationSerializer, AddressSerializer, AmenitySerializer


class AmenitiesListCreateView(ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer


class AddressListCreateView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class LocationListCreateView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

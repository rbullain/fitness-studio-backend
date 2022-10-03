from rest_framework import serializers

from apps.locations.models import Amenity, Location


class AmenityReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        exclude = ('id',)


class LocationReadSerializer(serializers.ModelSerializer):
    amenities = AmenityReadSerializer(many=True)
    address = serializers.StringRelatedField()

    class Meta:
        model = Location
        exclude = ('id',)

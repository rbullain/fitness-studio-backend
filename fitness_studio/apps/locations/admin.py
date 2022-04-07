from django.contrib import admin

from apps.locations.models import Location, Room, Address


@admin.register(Location, Room, Address)
class LocationsAdmin(admin.ModelAdmin):
    pass

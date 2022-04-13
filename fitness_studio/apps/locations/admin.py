from django.contrib import admin

from apps.locations.models import Location, Room, Address, Amenity


@admin.register(Address, Amenity)
class LocationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ('name', 'location__name',)
    list_display = ('name', 'location',)


class RoomInline(admin.TabularInline):
    model = Room
    extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address',)
    inlines = (RoomInline,)

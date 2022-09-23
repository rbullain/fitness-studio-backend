# -*- coding: utf-8 -*-
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """Address model."""
    address_line_1 = models.CharField(_('address line 1'), max_length=255, blank=True)
    address_line_2 = models.CharField(_('address line 2'), max_length=255, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    postal_code = models.CharField(_('postal code'), max_length=12, blank=True)
    country = CountryField(_('country'))

    longitude = models.DecimalField(_('longitude'), max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(_('latitude'), max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        ordering = ('pk',)
        verbose_name_plural = _("addresses")

    def __str__(self):
        return ", ".join([self.address_line_1, self.city, self.postal_code])


class Amenity(models.Model):
    """Amenity available on a location."""
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name_plural = _('amenities')

    def __str__(self):
        return self.name


class Location(models.Model):
    """A location, usually a building."""
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    amenities = models.ManyToManyField('locations.Amenity', related_name='locations', blank=True,
        verbose_name=_('amenities'))

    address = models.ForeignKey('locations.Address', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name=_('address'))

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Room(models.Model):
    """A room where a class is held."""
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE, related_name='rooms',
        verbose_name=_('location'))

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        ordering = ('name',)
        unique_together = (('name', 'location'),)

    def __str__(self):
        return self.name

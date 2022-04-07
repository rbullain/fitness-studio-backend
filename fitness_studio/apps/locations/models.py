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

    def __str__(self):
        return ", ".join([self.address_line_1, self.city, self.postal_code])


class Location(models.Model):
    """A location, usually a building."""
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    address = models.ForeignKey('locations.Address', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('address'))

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Room(models.Model):
    """A room where a class is held."""
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE, verbose_name=_('location'), related_name='rooms')

    class Meta:
        ordering = ('name',)
        unique_together = (('name', 'location'),)

    def __str__(self):
        return self.name

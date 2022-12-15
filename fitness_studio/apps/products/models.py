# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from versatileimagefield.fields import VersatileImageField, PPOIField

from apps.core.models import NameDescriptionModel


class ProductCategory(models.Model):
    """The category of a product."""
    name = models.CharField(_('name'), max_length=50)

    class Meta:
        verbose_name_plural = _("product categories")
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProductMedia(models.Model):
    """Media content of a product."""
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='media',
        verbose_name=_('product'))

    image = VersatileImageField(_('image'), upload_to='images/products/', ppoi_field='ppoi')
    alt = models.CharField(max_length=128, blank=True)
    ppoi = PPOIField()

    class Meta:
        verbose_name = _('product media')
        verbose_name_plural = _('product media')

    def __str__(self):
        return f"{self.pk} {self.product}"


class Product(NameDescriptionModel, TimeStampedModel):
    """Contains information about a product."""
    category = models.ForeignKey('products.ProductCategory', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name=_('category'))

    class Meta:
        ordering = ('name',)

from django.db import models
from django.utils.translation import gettext_lazy as _


class NameDescriptionModel(models.Model):
    """An abstract base class model that provides name and description fields."""
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)

    class Meta:
        abstract = True

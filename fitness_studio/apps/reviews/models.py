# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django_extensions.db.models import TimeStampedModel


class Review(TimeStampedModel):
    """A user review for some object."""
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_('content type'))
    object_id = models.PositiveIntegerField(_('object ID'))
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name=_('user'))

    comment = models.TextField(_('comment'), max_length=200)
    rating = models.PositiveSmallIntegerField(_('rating'))

    class Meta:
        ordering = ('-created', '-modified',)

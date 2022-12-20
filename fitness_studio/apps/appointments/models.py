from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Appointment(models.Model):
    """Information about a user appointment to a Class or a Service."""

    class Status(models.TextChoices):
        BOOKED = ("Booked", _("Booked"))
        CONFIRMED = ("Confirmed", _("Confirmed"))
        NO_SHOW = ("No show", _("No show"))
        CANCELLED = ("Cancelled", _("Cancelled"))
        __empty__ = _("None")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        related_name='appointments', verbose_name=_('user'))
    class_instance = models.ForeignKey('classes.ClassInstance', on_delete=models.SET_NULL, null=True,
        related_name='appointments', verbose_name=_('class instance'))

    status = models.CharField(_('status'), max_length=9, choices=Status.choices, null=True, blank=True)
    start_datetime = models.DateTimeField(_('start datetime'))
    end_datetime = models.DateTimeField(_('end datetime'))

    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='appointments_provided', verbose_name=_('staff'))
    location = models.ForeignKey('locations.Location', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='appointments', verbose_name=_('location'))

    def clean(self):
        super(Appointment, self).clean()

        if self.start_datetime > self.end_datetime:
            raise ValidationError("The start datetime must be earlier than the end datetime")

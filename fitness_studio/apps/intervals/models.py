from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.core.models import NameDescriptionModel


class Interval(NameDescriptionModel):
    """Contains information about an interval."""
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))

    def clean(self):
        super(Interval, self).clean()

        if self.start_date > self.end_date:
            raise ValidationError("The start date must be earlier than the end date")

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import NameDescriptionModel


class Interval(NameDescriptionModel):
    """Contains information about an interval."""
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))

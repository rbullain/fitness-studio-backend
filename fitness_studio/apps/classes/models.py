from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField, PPOIField
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
from dateutil.rrule import MO, TU, WE, TH, FR, SA, SU


class ClassCategory(models.Model):
    """The category of a class."""
    name = models.CharField(_('name'), max_length=50, unique=True)
    image = VersatileImageField(_('image'), upload_to='images/categories/', null=True, blank=True)

    class Meta:
        verbose_name_plural = _("class categories")
        ordering = ('name',)

    def __str__(self):
        return self.name


class ClassDescriptionMedia(models.Model):
    """Media content of a class."""
    class_description = models.ForeignKey('classes.ClassDescription', on_delete=models.CASCADE, related_name='media',
        verbose_name=_('class description'))

    image = VersatileImageField(_('image'), upload_to='images/classes/', ppoi_field='ppoi')
    alt = models.CharField(max_length=128, blank=True)
    ppoi = PPOIField()

    class Meta:
        verbose_name = _('class media')
        verbose_name_plural = _('class media')

    def __str__(self):
        return f"{self.pk} {self.class_description}"


class ClassDescription(TitleDescriptionModel, TimeStampedModel):
    """Contains information about a class."""
    category = models.ForeignKey('classes.ClassCategory', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name=_('category'))

    class Meta:
        verbose_name = _('class description')
        ordering = ('-created', '-modified',)

    def __str__(self):
        return self.title


class ClassInstance(TimeStampedModel):
    """Contains information about a class instance."""
    class_description = models.ForeignKey('classes.ClassDescription', on_delete=models.CASCADE, related_name='classes',
        verbose_name=_('class description'))
    class_schedule = models.ForeignKey('classes.ClassSchedule', on_delete=models.CASCADE, null=True, blank=True,
        related_name='classes', verbose_name=_('class schedule'))

    start_datetime = models.DateTimeField(_('start datetime'))
    end_datetime = models.DateTimeField(_('end datetime'))

    location = models.ForeignKey('locations.Location', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='classes', verbose_name=_('location'))
    room = models.ForeignKey('locations.Room', on_delete=models.SET_NULL, null=True, blank=True, related_name='classes',
        verbose_name=_('room'))

    class Meta:
        verbose_name_plural = _("class instances")
        ordering = ('-created', '-modified',)

    def clean(self):
        super(ClassInstance, self).clean()

        if self.start_datetime > self.end_datetime:
            raise ValidationError("The start datetime must be earlier than the end datetime")

        if self.room and self.location:
            if self.room.location != self.location:
                raise ValidationError("The room location does not belongs to the specified location")

    @property
    def duration(self):
        """Get the duration in hours of the class."""
        delta = self.end_datetime - self.start_datetime
        return delta / 3600

    def __str__(self):
        return f"{self.class_description} Class at {self.start_datetime}"


class ClassSchedule(TimeStampedModel):
    """Contains information about a class schedule."""
    class_description = models.ForeignKey('classes.ClassDescription', on_delete=models.CASCADE,
        related_name='schedules', verbose_name=_('class description'))

    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'))
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))

    on_mondays = models.BooleanField(_('on mondays'), default=False, blank=True)
    on_tuesdays = models.BooleanField(_('on tuesday'), default=False, blank=True)
    on_wednesdays = models.BooleanField(_('on wednesday'), default=False, blank=True)
    on_thursdays = models.BooleanField(_('on thursdays'), default=False, blank=True)
    on_fridays = models.BooleanField(_('on fridays'), default=False, blank=True)
    on_saturdays = models.BooleanField(_('on saturdays'), default=False, blank=True)
    on_sundays = models.BooleanField(_('on sundays'), default=False, blank=True)

    location = models.ForeignKey('locations.Location', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='schedules', verbose_name=_('location'))
    room = models.ForeignKey('locations.Room', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='schedules', verbose_name=_('room'))

    class Meta:
        verbose_name = _('class schedule')
        ordering = ('-created', '-modified',)

    def clean(self):
        super(ClassSchedule, self).clean()

        if self.start_time > self.end_time:
            raise ValidationError("The start time must be earlier than the end time")
        if self.start_date > self.end_date:
            raise ValidationError("The start date must be earlier than the end date")
        if not (self.on_mondays or self.on_tuesdays or self.on_wednesdays or self.on_thursdays or self.on_fridays or
                self.on_saturdays or self.on_sundays):
            raise ValidationError("At least one day of the week is required")

        if self.room and self.location:
            if self.room.location != self.location:
                raise ValidationError("The room location does not belongs to the specified location")

    @property
    def weekdays(self):
        """Get the weekdays when the class schedule takes place."""
        weekdays = []
        if self.on_mondays:
            weekdays.append(MO)
        if self.on_tuesdays:
            weekdays.append(TU)
        if self.on_wednesdays:
            weekdays.append(WE)
        if self.on_thursdays:
            weekdays.append(TH)
        if self.on_fridays:
            weekdays.append(FR)
        if self.on_saturdays:
            weekdays.append(SA)
        if self.on_sundays:
            weekdays.append(SU)
        return weekdays

    def __str__(self):
        return f"{self.class_description} Class every {self.weekdays} at {self.start_time}"

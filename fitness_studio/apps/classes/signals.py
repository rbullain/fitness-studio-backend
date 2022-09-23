import datetime
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from dateutil.rrule import rrule, WEEKLY

from apps.classes.models import ClassSchedule, ClassInstance


@receiver(post_save, sender=ClassSchedule)
def on_class_schedule_update(instance: ClassSchedule, created, **kwargs):
    """"""
    weekdays = instance.weekdays

    if not created:
        # Delete classes that do not belong to the schedule weekdays
        dj_weekdays = [(wd.weekday + 1) % 7 + 1 for wd in weekdays]     # Django weekdays starts from the Sunday with value 1
        instance.classes.exclude(start_datetime__week_day__in=dj_weekdays).delete()

        # Delete classes that are not in the date interval
        instance.classes.filter(start_datetime__lt=instance.start_date, start_datetime__gt=instance.end_date).delete()

        # Update classes that belongs to the schedule
        for cl in instance.classes.all():  # type: ClassInstance
            cl.class_description = instance.class_description
            cl.start_datetime = datetime.datetime.combine(cl.start_datetime.date(), instance.start_time, timezone.get_current_timezone())
            cl.end_datetime = datetime.datetime.combine(cl.end_datetime.date(), instance.end_time, timezone.get_current_timezone())

            cl.save(update_fields=['class_description', 'start_datetime', 'end_datetime'])

    # Create class instances that are missing
    for dt in rrule(WEEKLY, dtstart=instance.start_date, until=instance.end_date, byweekday=weekdays):
        start_datetime = datetime.datetime.combine(dt, instance.start_time, timezone.get_current_timezone())
        end_datetime = datetime.datetime.combine(dt, instance.end_time, timezone.get_current_timezone())

        cl_obj, _ = instance.classes.get_or_create(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            defaults={
                'class_description': instance.class_description,
                'location': instance.location,
                'room': instance.room,
            }
        )

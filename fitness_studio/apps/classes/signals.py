from datetime import datetime
from dateutil.rrule import rrule, WEEKLY
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q

from apps.classes.models import ClassSchedule, ClassInstance


@receiver(post_save, sender=ClassSchedule)
def on_class_schedule_update(instance: ClassSchedule, created, **kwargs):
    """Update or delete related ClassInstance objects when a ClassSchedule is updated."""
    if kwargs.get('raw', False):
        # Avoid execution when loading fixtures
        return

    weekdays = instance.weekdays
    tz = timezone.get_current_timezone()

    if not created:
        # Delete classes that do not belong to the schedule weekdays
        dj_weekdays = [(wd.weekday + 1) % 7 + 1 for wd in weekdays]  # Django weekdays starts from Sunday with value 1
        instance.classes.exclude(start_datetime__week_day__in=dj_weekdays).delete()

        # Delete classes that are not in the date interval
        instance.classes.filter(Q(start_datetime__lt=instance.start_date) | Q(start_datetime__gt=instance.end_date)).delete()

        # Update classes time that belongs to the schedule
        fields_to_update = ['class_description', 'start_datetime', 'end_datetime']
        updated_classes_instances = [
            ClassInstance(
                id=cl.id,
                class_description=instance.class_description,
                start_datetime=datetime.combine(cl.start_datetime.date(), instance.start_time, tz),
                end_datetime=datetime.combine(cl.end_datetime.date(), instance.end_time, tz)
            ) for cl in instance.classes.all()
        ]

        ClassInstance.objects.bulk_update(updated_classes_instances, fields_to_update)

    # Create class instances that are missing
    create_classes_instances = []
    for dt in rrule(WEEKLY, dtstart=instance.start_date, until=instance.end_date, byweekday=weekdays):
        start_datetime = datetime.combine(dt, instance.start_time, tz)
        end_datetime = datetime.combine(dt, instance.end_time, tz)

        if not instance.classes.filter(start_datetime=start_datetime, end_datetime=end_datetime).exists():
            create_classes_instances.append(
                ClassInstance(
                    class_description=instance.class_description,
                    class_schedule=instance,
                    start_datetime=start_datetime,
                    end_datetime=end_datetime,
                    location=instance.location,
                    room=instance.room,
                )
            )

    ClassInstance.objects.bulk_create(create_classes_instances)

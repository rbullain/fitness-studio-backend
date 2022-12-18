import datetime
from dateutil.rrule import rrule, WEEKLY
from django.test import TestCase
from django.utils import timezone

from apps.classes.models import ClassSchedule


def assert_valid_schedule_instances(test_case: TestCase, schedule: ClassSchedule):
    """Fail if the ClassSchedule does not contain the valid instances."""
    tz = timezone.get_current_timezone()
    intervals = [
        (datetime.datetime.combine(dt, schedule.start_time, tz), datetime.datetime.combine(dt, schedule.end_time, tz))
        for dt in rrule(WEEKLY, dtstart=schedule.start_date, until=schedule.end_date, byweekday=schedule.weekdays)
    ]

    # Check amount of ClassInstances
    test_case.assertEqual(schedule.classes.count(), len(intervals))

    for i, instance in enumerate(schedule.classes.all().order_by('start_datetime')):
        test_case.assertEqual(instance.class_schedule, schedule)
        test_case.assertEqual(instance.class_description, schedule.class_description)

        test_case.assertEqual(instance.room, schedule.room)
        test_case.assertEqual(instance.location, schedule.location)

        test_case.assertEqual(instance.start_datetime, intervals[i][0])
        test_case.assertEqual(instance.end_datetime, intervals[i][1])

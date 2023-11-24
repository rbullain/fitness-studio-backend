import datetime
from django.test import TestCase
from django.utils import timezone
from dateutil.rrule import rrule, WEEKLY

from apps.classes.models import ClassSchedule


def _generate_intervals(start_date, end_date, weekdays, start_time, end_time, tz):
    """Generate a list of intervals within the specified dates and weekdays, each starting at `start_time` and ending
    at `end_time`."""
    return [
        (datetime.datetime.combine(dt, start_time, tz), datetime.datetime.combine(dt, end_time, tz))
        for dt in rrule(WEEKLY, dtstart=start_date, until=end_date, byweekday=weekdays)
    ]


def assert_valid_schedule_instances(test_case: TestCase, schedule: ClassSchedule):
    """Fail if the ClassSchedule does not contain the valid instances."""
    tz = timezone.get_current_timezone()
    intervals = _generate_intervals(schedule.start_date, schedule.end_date, schedule.weekdays, schedule.start_time,
        schedule.end_time, tz)

    # Check amount of ClassInstances
    test_case.assertEqual(schedule.classes.count(), len(intervals))

    for i, instance in enumerate(schedule.classes.all().order_by('start_datetime')):
        # Verify that each instance was well created
        test_case.assertEqual(instance.class_schedule, schedule)
        test_case.assertEqual(instance.class_description, schedule.class_description)

        test_case.assertEqual(instance.room, schedule.room)
        test_case.assertEqual(instance.location, schedule.location)

        # Verify instance interval
        test_case.assertEqual(instance.start_datetime, intervals[i][0])
        test_case.assertEqual(instance.end_datetime, intervals[i][1])

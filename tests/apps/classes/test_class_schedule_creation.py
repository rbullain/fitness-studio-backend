import datetime
from django.test import TestCase
from dateutil.rrule import rrule, WEEKLY
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.classes.models import ClassSchedule, ClassDescription
from apps.locations.models import Room, Location


class ClassScheduleCreationTestCase(TestCase):
    fixtures = ('app_classes_initial.json',)

    def assertValidScheduleInstances(self, schedule: ClassSchedule):
        """Fall if the ClassSchedule does not contain the valid instances."""
        tz = timezone.get_current_timezone()
        intervals = [
            (datetime.datetime.combine(dt, schedule.start_time, tz), datetime.datetime.combine(dt, schedule.end_time, tz))
            for dt in rrule(WEEKLY, dtstart=schedule.start_date, until=schedule.end_date, byweekday=schedule.weekdays)
        ]

        for i, instance in enumerate(schedule.classes.all().order_by('start_datetime')):
            self.assertEqual(instance.class_schedule, schedule)
            self.assertEqual(instance.class_description, schedule.class_description)

            self.assertEqual(instance.room, schedule.room)
            self.assertEqual(instance.location, schedule.location)

            self.assertEqual(instance.start_datetime, intervals[i][0])
            self.assertEqual(instance.end_datetime, intervals[i][1])

    def test_create_schedule_one_weekday(self):
        """Test if a schedule, and all its instances are successfully created with one weekday."""
        schedule = {
            'class_description': ClassDescription.objects.get(pk=1),
            'start_date': datetime.date(2022, 10, 10),
            'end_date': datetime.date(2022, 11, 10),
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
            'on_mondays': True,
        }

        schedule_obj = ClassSchedule(**schedule)
        schedule_obj.save()

        self.assertValidScheduleInstances(schedule_obj)

    def test_create_schedule_multiple_weekdays(self):
        """Test if a schedule, and all its instances are successfully created with more than
        one weekday."""
        schedule = {
            'class_description': ClassDescription.objects.get(pk=1),
            'start_date': datetime.date(2022, 10, 10),
            'end_date': datetime.date(2022, 11, 10),
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
            'on_mondays': True,
            'on_wednesdays': True,
            'on_saturdays': True,
        }

        schedule_obj = ClassSchedule(**schedule)
        schedule_obj.save()

        self.assertValidScheduleInstances(schedule_obj)

    def test_create_schedule_no_weekday(self):
        """Test if an exception is raised when no `weekday` is defined."""
        schedule = {
            'class_description': ClassDescription.objects.get(pk=1),
            'start_date': datetime.date(2022, 10, 10),
            'end_date': datetime.date(2022, 11, 10),
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
        }

        with self.assertRaises(ValidationError):
            schedule_obj = ClassSchedule(**schedule)
            schedule_obj.clean()

    def test_create_schedule_start_date_greater_than_end_date(self):
        """Test if an exception is raised when the `start_date` is greater than the `end_date`."""
        schedule = {
            'class_description': ClassDescription.objects.get(pk=1),
            'start_date': datetime.date(2022, 11, 10),
            'end_date': datetime.date(2022, 10, 10),
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
            'on_mondays': True,
        }

        with self.assertRaises(ValidationError):
            schedule_obj = ClassSchedule(**schedule)
            schedule_obj.clean()

    def test_create_schedule_invalid_room_location(self):
        """Test if an exception is raised when a `location` and a `room` belonging to a different
        location are defined at the same time during cleaning."""
        schedule = {
            'class_description': ClassDescription.objects.get(pk=1),
            'location': Location.objects.get(pk=2),
            'room': Room.objects.get(pk=1),
            'start_date': datetime.date(2022, 11, 10),
            'end_date': datetime.date(2022, 10, 10),
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
            'on_mondays': True,
        }

        with self.assertRaises(ValidationError):
            schedule_obj = ClassSchedule(**schedule)
            schedule_obj.clean()

import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.classes.models import ClassDescription, ClassSchedule
from apps.locations.models import Location, Room


class ClassScheduleValidationTestCase(TestCase):
    fixtures = ('app_classes_initial.json',)

    def test_create_schedule_no_weekday(self):
        """Test if an exception is raised when no `weekday` is defined."""
        schedule_data = {
            'class_description': ClassDescription.objects.get(pk=1),
            'start_date': datetime.date(2022, 10, 10),
            'end_date': datetime.date(2022, 11, 10),
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
        }

        with self.assertRaises(ValidationError):
            schedule_obj = ClassSchedule(**schedule_data)
            schedule_obj.clean()

    def test_create_schedule_start_time_greater_than_end_time(self):
        """Test if an exception is raised when the `start_time` is greater than the `end_time`."""
        schedule_data = {
            'class_description': ClassDescription.objects.get(pk=1),
            'start_date': datetime.date(2022, 11, 10),
            'end_date': datetime.date(2022, 10, 10),
            'start_time': datetime.time(hour=10, minute=30),
            'end_time': datetime.time(hour=10),
            'on_mondays': True,
        }

        with self.assertRaises(ValidationError):
            schedule_obj = ClassSchedule(**schedule_data)
            schedule_obj.clean()

    def test_create_schedule_start_date_greater_than_end_date(self):
        """Test if an exception is raised when the `start_date` is greater than the `end_date`."""
        schedule_data = {
            'class_description': ClassDescription.objects.get(pk=1),
            'start_date': datetime.date(2022, 11, 10),
            'end_date': datetime.date(2022, 10, 10),
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
            'on_mondays': True,
        }

        with self.assertRaises(ValidationError):
            schedule_obj = ClassSchedule(**schedule_data)
            schedule_obj.clean()

    def test_create_schedule_invalid_room_location(self):
        """Test if an exception is raised when a `location` and a `room` belonging to a different
        location are defined at the same time during cleaning."""
        schedule_data = {
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
            schedule_obj = ClassSchedule(**schedule_data)
            schedule_obj.clean()

import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.classes.models import ClassSchedule, ClassDescription
from apps.locations.models import Location, Room
from tests.apps.classes.utils import assert_valid_schedule_instances


class ClassScheduleCreationTestCase(TestCase):
    fixtures = ('app_classes_initial.json',)

    def setUp(self):
        self.class_description = ClassDescription.objects.get(pk=1)
        self.start_date = datetime.date(2022, 10, 10)  # 2022-10-10
        self.end_date = datetime.date(2022, 11, 10)  # 2022-11-10

    def test_create_schedule_one_weekday(self):
        """Test if a schedule, and all its instances are successfully created with one weekday."""
        schedule_data = {
            'class_description': self.class_description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
            'on_mondays': True,
        }

        schedule_obj = ClassSchedule(**schedule_data)
        schedule_obj.save()

        assert_valid_schedule_instances(self, schedule_obj)

    def test_create_schedule_multiple_weekdays(self):
        """Test if a schedule, and all its instances are successfully created with more than
        one weekday."""
        schedule_data = {
            'class_description': self.class_description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'start_time': datetime.time(hour=10),
            'end_time': datetime.time(hour=10, minute=30),
            'on_mondays': True,
            'on_wednesdays': True,
            'on_saturdays': True,
        }

        schedule_obj = ClassSchedule(**schedule_data)
        schedule_obj.save()

        assert_valid_schedule_instances(self, schedule_obj)


class ClassScheduleCreationValidationTestCase(TestCase):
    fixtures = ('app_classes_initial.json',)

    def setUp(self):
        self.class_description = ClassDescription.objects.get(pk=1)
        self.start_date = datetime.date(2022, 10, 10)  # 2022-10-10
        self.start_time = datetime.time(hour=10)  # 10:00:00
        self.end_date = datetime.date(2022, 11, 10)  # 2022-11-10
        self.end_time = datetime.time(hour=10, minute=30)  # 10:30:00

    @staticmethod
    def _create_and_clean_schedule(**kwargs):
        """Helper method to create and validate a ClassSchedule object."""
        schedule_obj = ClassSchedule(**kwargs)
        schedule_obj.clean()

        return schedule_obj

    def test_create_schedule_no_weekday(self):
        """Test if an exception is raised when no `weekday` is defined."""
        schedule_data = {
            'class_description': self.class_description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'start_time': self.start_time,
            'end_time': self.end_time,
        }

        with self.assertRaises(ValidationError):
            self._create_and_clean_schedule(**schedule_data)

    def test_create_schedule_start_time_greater_than_end_time(self):
        """Test if an exception is raised when the `start_time` is greater than the `end_time`."""
        schedule_data = {
            'class_description': self.class_description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'start_time': self.end_time,
            'end_time': self.start_time,
            'on_mondays': True,
        }

        with self.assertRaises(ValidationError):
            self._create_and_clean_schedule(**schedule_data)

    def test_create_schedule_start_date_greater_than_end_date(self):
        """Test if an exception is raised when the `start_date` is greater than the `end_date`."""
        schedule_data = {
            'class_description': self.class_description,
            'start_date': self.end_date,
            'end_date': self.start_date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'on_mondays': True,
        }

        with self.assertRaises(ValidationError):
            self._create_and_clean_schedule(**schedule_data)

    def test_create_schedule_invalid_room_location(self):
        """Test if an exception is raised when a `location` and a `room` belonging to a different
        location are defined at the same time during cleaning."""

        location = Location.objects.get(pk=2)
        room = Room.objects.get(pk=1)

        # Ensure that the room does not belong to the location
        self.assertNotIn(room, location.rooms.all())

        schedule_data = {
            'class_description': self.class_description,
            'location': location,
            'room': room,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'on_mondays': True,
        }

        with self.assertRaises(ValidationError):
            self._create_and_clean_schedule(**schedule_data)

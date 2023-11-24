import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.classes.models import ClassInstance, ClassDescription
from apps.locations.models import Location, Room


class ClassInstanceCreationTestCase(TestCase):
    fixtures = ('app_classes_initial.json',)

    def setUp(self):
        self.class_description = ClassDescription.objects.get(pk=1)
        self.start_datetime = datetime.datetime(2022, 11, 10, 10, 00)  # 2022-10-21 10:00:00
        self.end_datetime = datetime.datetime(2022, 11, 10, 10, 30)  # 2022-10-21 10:30:00

    def test_create_instance(self):
        """Test if a minimal instance is successfully created."""
        instance_data = {
            'class_description': self.class_description,
            'start_datetime': self.start_datetime,
            'end_datetime': self.end_datetime,
        }

        instance_obj = ClassInstance(**instance_data)
        instance_obj.save()

        self.assertEqual(instance_obj.class_description, self.class_description)
        self.assertEqual(instance_obj.start_datetime, self.start_datetime)
        self.assertEqual(instance_obj.end_datetime, self.end_datetime)


class ClassInstanceCreationValidationTestCase(TestCase):
    fixtures = ('app_classes_initial.json',)

    def setUp(self):
        self.class_description = ClassDescription.objects.get(pk=1)
        self.start_datetime = datetime.datetime(2022, 11, 10, 10, 00)  # 2022-10-21 10:00:00
        self.end_datetime = datetime.datetime(2022, 11, 10, 10, 30)  # 2022-10-21 10:30:00

    @staticmethod
    def _create_and_clean(**kwargs):
        """Helper method to create and validate a ClassInstance object."""
        instance_obj = ClassInstance(**kwargs)
        instance_obj.clean()

        return instance_obj

    def test_create_instance_start_datetime_greater_than_end_datetime(self):
        """Test if an exception is raised when the `start_datetime` is greater than the `end_datetime`."""
        instance_data = {
            'class_description': self.class_description,
            'start_datetime': self.end_datetime,
            'end_datetime': self.start_datetime,
        }

        with self.assertRaises(ValidationError):
            self._create_and_clean(**instance_data)

    def test_create_instance_invalid_room_location(self):
        """Test if an exception is raised when a `location` and a `room` belonging to a different
        location are defined at the same time during cleaning."""

        location = Location.objects.get(pk=2)
        room = Room.objects.get(pk=1)

        # Ensure that the room does not belong to the location
        self.assertNotIn(room, location.rooms.all())

        instance_data = {
            'class_description': self.class_description,
            'location': location,
            'room': room,
            'start_datetime': self.start_datetime,
            'end_datetime': self.end_datetime,
        }

        with self.assertRaises(ValidationError):
            self._create_and_clean(**instance_data)

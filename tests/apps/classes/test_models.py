import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.classes.models import ClassSchedule, ClassDescription
from apps.locations.models import Room, Location


class ClassScheduleTestCase(TestCase):
    fixtures = ('app_classes_initial.json',)

    def test_invalid_schedule_no_weekday(self):
        """Test if an exception is raised when no `weekday` is defined during cleaning."""
        schedule_obj = ClassSchedule(
            class_description=ClassDescription.objects.get(pk=1),
            start_date=datetime.date(2022, 10, 10),
            end_date=datetime.date(2022, 11, 10),
            start_time=datetime.time(hour=10),
            end_time=datetime.time(hour=10, minute=30),
        )
        self.assertRaises(ValidationError, schedule_obj.clean)

    def test_invalid_schedule_invalid_dates(self):
        """Test if an exception is raised when the `start_date` is greater than the `end_date`
        during cleaning."""
        schedule_obj = ClassSchedule(
            class_description=ClassDescription.objects.get(pk=1),
            start_date=datetime.date(2022, 11, 10),
            end_date=datetime.date(2022, 10, 10),
            start_time=datetime.time(hour=10),
            end_time=datetime.time(hour=10, minute=30),
            on_mondays=True,
        )
        self.assertRaises(ValidationError, schedule_obj.clean)

    def test_invalid_schedule_invalid_room_location(self):
        """Test if an exception is raised when a `location` and a `room` belonging to a different
        location are defined at the same time during cleaning."""
        schedule_obj = ClassSchedule(
            class_description=ClassDescription.objects.get(pk=1),
            location=Location.objects.get(pk=2),
            room=Room.objects.get(pk=1),
            start_date=datetime.date(2022, 11, 10),
            end_date=datetime.date(2022, 10, 10),
            start_time=datetime.time(hour=10),
            end_time=datetime.time(hour=10, minute=30),
            on_mondays=True,
        )
        self.assertRaises(ValidationError, schedule_obj.clean)

    def test_schedule_instances_creation(self):
        """Test if every instance created by the schedule is properly initialized."""
        schedule_obj = ClassSchedule(
            class_description=ClassDescription.objects.get(pk=1),
            location=Location.objects.get(pk=1),
            room=Room.objects.get(pk=1),
            start_date=datetime.date(2022, 10, 10),
            end_date=datetime.date(2022, 11, 10),
            start_time=datetime.time(hour=10),
            end_time=datetime.time(hour=10, minute=30),
            on_mondays=True,
        )
        schedule_obj.save()

        self.assertIsNotNone(schedule_obj.classes)
        self.assertEqual(schedule_obj.classes.count(), 5)

        # Every Monday date between the 10-10-2022 and the 10-11-2022
        tzinfo = timezone.get_current_timezone()
        start_intervals = [datetime.datetime(2022, 10, 10, 10, tzinfo=tzinfo),
            datetime.datetime(2022, 10, 17, 10, tzinfo=tzinfo),
            datetime.datetime(2022, 10, 24, 10, tzinfo=tzinfo),
            datetime.datetime(2022, 10, 31, 10, tzinfo=tzinfo),
            datetime.datetime(2022, 11, 7, 10, tzinfo=tzinfo)]
        end_intervals = [datetime.datetime(2022, 10, 10, 10, 30, tzinfo=tzinfo),
            datetime.datetime(2022, 10, 17, 10, 30, tzinfo=tzinfo),
            datetime.datetime(2022, 10, 24, 10, 30, tzinfo=tzinfo),
            datetime.datetime(2022, 10, 31, 10, 30, tzinfo=tzinfo),
            datetime.datetime(2022, 11, 7, 10, 30, tzinfo=tzinfo)]

        for i, instance in enumerate(schedule_obj.classes.all().order_by('start_datetime')):
            self.assertEqual(instance.class_schedule, schedule_obj)
            self.assertEqual(instance.class_description, schedule_obj.class_description)

            # Verify location
            self.assertEqual(instance.room, schedule_obj.room)
            self.assertEqual(instance.location, schedule_obj.location)

            # Verify intervals
            self.assertEqual(instance.start_datetime, start_intervals[i])
            self.assertEqual(instance.end_datetime, end_intervals[i])

import datetime
from django.test import TestCase

from apps.classes.models import ClassSchedule
from tests.apps.classes.utils import assert_valid_schedule_instances


class ClassScheduleUpdateTestCase(TestCase):
    fixtures = ('app_classes_schedule.json',)

    def setUp(self):
        self.schedule_obj = ClassSchedule.objects.get(id=1)

    def test_update_schedule_interval_increase_add_classes_instances(self):
        """Test if all the necessary instances are created when the interval is increased."""
        self.schedule_obj.start_date = datetime.date(year=2022, month=9, day=26)  # From 2022-10-01
        self.schedule_obj.save()

        assert_valid_schedule_instances(self, self.schedule_obj)

    def test_update_schedule_interval_decrease_delete_classes_instances(self):
        """Test if all instances that does not belong to the interval are deleted when a date
        is reduced."""
        self.schedule_obj.end_date = datetime.date(year=2022, month=10, day=5)  # From 2022-10-21
        self.schedule_obj.save()

        assert_valid_schedule_instances(self, self.schedule_obj)

from rest_framework import viewsets

from apps.classes.models import ClassDescription, ClassCategory, ClassSchedule, ClassInstance
from api.classes import serializers


class ClassCategoryReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassCategory.objects.all()
    serializer_class = serializers.ClassCategoryReadSerializer


class ClassDescriptionReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassDescription.objects.all()
    serializer_class = serializers.ClassDescriptionReadSerializer
    filterset_fields = {
        # TODO: Add filter by dates of related instance classes.
    }


class ClassScheduleReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassSchedule.objects.all()
    serializer_class = serializers.ClassScheduleReadSerializer
    filterset_fields = {
        'class_description': ['in'],
        'location': ['in'],
    }


class ClassInstanceReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassInstance.objects.all()
    serializer_class = serializers.ClassInstanceReadSerializer
    filterset_fields = {
        'class_description': ['in'],
        'class_schedule': ['in'],
        'start_datetime': ['gte', 'lte'],
        'location': ['in'],
        'modified': ['gte'],
    }

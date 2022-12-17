from rest_framework import viewsets

from api.core.mixins import SerializerActionViewSetMixin
from apps.classes.models import ClassDescription, ClassCategory, ClassSchedule, ClassInstance
from api.classes import serializers


class ClassCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClassCategory.objects.all()
    serializer_class = serializers.ClassCategoryReadSerializer


class ClassDescriptionViewSet(viewsets.ModelViewSet):
    queryset = ClassDescription.objects.all()
    serializer_class = serializers.ClassDescriptionReadSerializer
    filterset_fields = {
        # TODO: Add filter by dates of related instance classes.
    }


class ClassScheduleViewSet(SerializerActionViewSetMixin, viewsets.ModelViewSet):
    queryset = ClassSchedule.objects.all()
    serializer_action_classes = {
        'create': serializers.ClassScheduleCreateSerializer,
        'update': serializers.ClassScheduleUpdateSerializer,
    }
    default_serializer_class = serializers.ClassScheduleReadSerializer
    filterset_fields = {
        'class_description': ['in'],
        'location': ['in'],
    }


class ClassInstanceViewSet(viewsets.ModelViewSet):
    queryset = ClassInstance.objects.all()
    serializer_class = serializers.ClassInstanceReadSerializer
    filterset_fields = {
        'class_description': ['in'],
        'class_schedule': ['in'],
        'start_datetime': ['gte', 'lte'],
        'location': ['in'],
        'modified': ['gte'],
    }

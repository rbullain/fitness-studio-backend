from rest_framework import viewsets

from apps.classes.models import ClassCategory, ClassDescription, ClassSchedule, ClassInstance
from api.classes import serializers


class ClassCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassCategory.objects.all()
    serializer_class = serializers.ClassCategorySerializer


class ClassDescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassDescription.objects.all()
    serializer_class = serializers.ClassDescriptionSerializer


class ClassScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassSchedule.objects.all()
    serializer_class = serializers.ClassScheduleSerializer


class ClassInstanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassInstance.objects.all()
    serializer_class = serializers.ClassInstanceSerializer

from rest_framework import viewsets

from apps.classes.models import ClassDescription, ClassCategory, ClassSchedule, ClassInstance
from api.classes import serializers


class ClassCategoryReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassCategory.objects.all()
    serializer_class = serializers.ClassCategoryReadSerializer
    lookup_field = 'slug'


class ClassDescriptionReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassDescription.objects.all()
    serializer_class = serializers.ClassDescriptionReadSerializer
    lookup_field = 'slug'


class ClassScheduleReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassSchedule.objects.all()
    serializer_class = serializers.ClassScheduleReadSerializer


class ClassInstanceReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassInstance.objects.all()
    serializer_class = serializers.ClassInstanceReadSerializer

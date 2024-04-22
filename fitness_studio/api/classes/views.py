from datetime import datetime

from rest_framework.generics import ListAPIView, ListCreateAPIView

from apps.classes.models import ClassCategory, ClassDescription, ClassSchedule, ClassInstance
from api.classes.filters import ClassDescriptionFilterSet, ClassScheduleFilterSet, ClassInstanceFilterSet
from api.classes.serializers import ClassDescriptionSerializer, ClassScheduleSerializer, ClassInstanceSerializer, \
    ClassCategorySerializer


class ClassCategoryListCreateView(ListCreateAPIView):
    queryset = ClassCategory.objects.all()
    serializer_class = ClassCategorySerializer


class ClassDescriptionListCreateView(ListCreateAPIView):
    queryset = ClassDescription.objects.all()
    serializer_class = ClassDescriptionSerializer
    filterset_class = ClassDescriptionFilterSet


class ClassScheduleListCreateView(ListCreateAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer
    filterset_class = ClassScheduleFilterSet

    def filter_queryset(self, queryset):
        # Handle the case if the filter for `start_date` or `end_date` are not set.
        # If `start_date` is not set then it filters from the current date.
        # If `end_date` is not set then it filters from the `start_date`.
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        now = datetime.now()

        if start_date is None and end_date is None:
            queryset = queryset.filter(start_date=now)
        elif start_date is None:
            queryset = queryset.filter(start_date__gte=now)
        elif end_date is None:
            queryset = queryset.filter(start_date__lte=start_date)

        return queryset


class ClassInstanceListCreateView(ListCreateAPIView):
    queryset = ClassInstance.objects.all()
    serializer_class = ClassInstanceSerializer
    filterset_class = ClassInstanceFilterSet

    def filter_queryset(self, queryset):
        # Handle the case if the filter for `start_datetime` or `end_datetime` are not set.
        # If `start_datetime` is not set then it filters from the current datetime.
        # If `end_datetime` is not set then it filters from the `start_datetime` date.
        start_datetime = self.request.query_params.get('start_datetime')
        end_datetime = self.request.query_params.get('end_datetime')
        now = datetime.now()

        if start_datetime is None and end_datetime is None:
            queryset = queryset.filter(start_datetime__date=now)
        elif start_datetime is None:
            queryset = queryset.filter(start_datetime__gte=now)
        elif end_datetime is None:
            queryset = queryset.filter(start_datetime__date__lte=start_datetime)

        return queryset

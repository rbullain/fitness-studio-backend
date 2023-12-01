from django_filters import FilterSet, filters

from apps.classes.models import ClassDescription, ClassInstance, ClassSchedule


class ClassDescriptionFilterSet(FilterSet):
    class_description_ids = filters.BaseCSVFilter(field_name='pk', lookup_expr='in')
    location_ids = filters.BaseCSVFilter(field_name='location', lookup_expr='in')
    category_ids = filters.BaseCSVFilter(field_name='category', lookup_expr='in')
    last_modified = filters.DateTimeFilter(field_name='modified', lookup_expr='gte')

    class Meta:
        model = ClassDescription
        fields = ('class_description_ids', 'location_ids', 'category_ids', 'last_modified',)


class ClassScheduleFilterSet(FilterSet):
    class_schedule_ids = filters.BaseCSVFilter(field_name='pk', lookup_expr='in')
    class_description_ids = filters.BaseCSVFilter(field_name='class_description', lookup_expr='in')
    location_ids = filters.BaseCSVFilter(field_name='location', lookup_expr='in')
    start_date = filters.DateTimeFilter(field_name='start_date', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='start_date', lookup_expr='lte')
    last_modified = filters.DateTimeFilter(field_name='modified', lookup_expr='gte')

    class Meta:
        model = ClassSchedule
        fields = (
            'class_schedule_ids', 'class_description_ids', 'location_ids', 'start_date', 'end_date', 'last_modified',
        )


class ClassInstanceFilterSet(FilterSet):
    class_instance_ids = filters.BaseCSVFilter(field_name='pk', lookup_expr='in')
    class_description_ids = filters.BaseCSVFilter(field_name='class_description', lookup_expr='in')
    class_schedule_ids = filters.BaseCSVFilter(field_name='class_schedule', lookup_expr='in')
    location_ids = filters.BaseCSVFilter(field_name='location', lookup_expr='in')
    start_datetime = filters.DateTimeFilter(field_name='start_datetime', lookup_expr='gte')
    end_datetime = filters.DateTimeFilter(field_name='start_datetime', lookup_expr='lte')
    last_modified = filters.DateTimeFilter(field_name='modified', lookup_expr='gte')

    class Meta:
        model = ClassInstance
        fields = (
            'class_instance_ids', 'class_description_ids', 'class_schedule_ids', 'location_ids', 'start_datetime',
            'end_datetime', 'last_modified',
        )

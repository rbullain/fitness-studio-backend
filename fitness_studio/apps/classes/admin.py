from django.contrib import admin
from apps.classes.models import ClassInstance, ClassDescription, ClassSchedule, ClassCategory, ClassDescriptionMedia


@admin.register(ClassCategory, ClassDescriptionMedia)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'weekdays', 'start_time', 'end_time',)

    def title(self, instance):
        return instance.class_description.title


@admin.register(ClassDescription)
class ClassDescriptionAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category__name',)
    list_display = ('title', 'category',)


@admin.register(ClassInstance)
class ClassInstanceAdmin(admin.ModelAdmin):
    search_fields = ('class_description__title',)
    list_display = ('title', 'start_datetime', 'location',)

    def title(self, instance):
        return instance.class_description.title

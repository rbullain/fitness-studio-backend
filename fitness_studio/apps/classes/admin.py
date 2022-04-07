from django.contrib import admin
from apps.classes.models import ClassInstance, ClassDescription, ClassSchedule, ClassCategory


@admin.register(ClassInstance, ClassDescription, ClassSchedule, ClassCategory)
class ClassAdmin(admin.ModelAdmin):
    pass

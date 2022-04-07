from django.contrib import admin
from apps.classes.models import ClassInstance, ClassDescription, ClassSchedule, ClassCategory, ClassDescriptionMedia


@admin.register(ClassInstance, ClassDescription, ClassSchedule, ClassCategory, ClassDescriptionMedia)
class ClassAdmin(admin.ModelAdmin):
    pass

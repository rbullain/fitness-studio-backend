from django.contrib import admin
from apps.classes.models import ClassInstance, ClassDescription, ClassSchedule, ClassCategory, ClassDescriptionMedia


@admin.register(ClassInstance, ClassSchedule, ClassCategory, ClassDescriptionMedia)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassDescription)
class ClassDescriptionAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category__name',)
    list_display = ('title', 'category',)

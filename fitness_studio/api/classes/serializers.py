from rest_framework import serializers

from apps.classes.models import ClassCategory, ClassDescription, ClassInstance, ClassSchedule


class ClassCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        exclude = ('id',)


class ClassDescriptionReadSerializer(serializers.ModelSerializer):
    category = ClassCategoryReadSerializer()

    class Meta:
        model = ClassDescription
        exclude = ('id', 'created',)

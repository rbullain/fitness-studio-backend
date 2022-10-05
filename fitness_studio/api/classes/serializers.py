from rest_framework import serializers

from apps.classes.models import ClassCategory, ClassDescription, ClassInstance, ClassSchedule


class ClassCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        fields = '__all__'


class ClassDescriptionReadSerializer(serializers.ModelSerializer):
    category = ClassCategoryReadSerializer()

    class Meta:
        model = ClassDescription
        exclude = ('created',)


class ClassScheduleReadSerializer(serializers.ModelSerializer):
    class_description = ClassDescriptionReadSerializer()

    class Meta:
        model = ClassSchedule
        exclude = ('created',)


class ClassInstanceReadSerializer(serializers.ModelSerializer):
    class_description = ClassDescriptionReadSerializer()

    class Meta:
        model = ClassInstance
        exclude = ('created',)

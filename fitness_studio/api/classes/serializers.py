from rest_framework import serializers

from apps.classes.models import ClassDescription, ClassSchedule, ClassInstance


class ClassDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDescription
        exclude = ('created',)


class ClassScheduleSerializer(serializers.ModelSerializer):
    classes = serializers.PrimaryKeyRelatedField(queryset=ClassInstance.objects.all(), many=True)

    class Meta:
        model = ClassSchedule
        exclude = ('created', 'room',)


class ClassInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInstance
        exclude = ('created', 'room',)

from rest_framework import serializers

from apps.classes.models import ClassCategory, ClassDescription, ClassSchedule, ClassInstance


class ClassCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        fields = '__all__'


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

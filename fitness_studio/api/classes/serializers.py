from rest_framework import serializers

from apps.classes.models import ClassCategory, ClassDescription, ClassSchedule, ClassInstance


class ClassCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        fields = '__all__'


class ClassDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDescription
        fields = '__all__'


class ClassScheduleSerializer(serializers.ModelSerializer):
    classes = serializers.PrimaryKeyRelatedField(queryset=ClassInstance.objects.all(), many=True)

    class Meta:
        model = ClassSchedule
        fields = '__all__'


class ClassInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInstance
        fields = '__all__'

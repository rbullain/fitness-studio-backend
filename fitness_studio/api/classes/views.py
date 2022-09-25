from rest_framework import viewsets

from api.classes.serializers import ClassInstanceSerializer
from apps.classes.models import ClassInstance


class ClassInstanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClassInstance.objects.all()
    serializer_class = ClassInstanceSerializer

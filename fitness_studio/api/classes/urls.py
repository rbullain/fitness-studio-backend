from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.classes import views

router = DefaultRouter()
router.register('categories', views.ClassCategoryReadViewSet, basename='class-categories')
router.register('descriptions', views.ClassDescriptionReadViewSet, basename='class-description')
router.register('schedules', views.ClassScheduleReadViewSet, basename='class-schedule')
router.register('instances', views.ClassInstanceReadViewSet, basename='class-instance')

urlpatterns = [
    path('', include(router.urls)),
]

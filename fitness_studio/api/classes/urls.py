from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.classes import views

router = DefaultRouter()
router.register('categories', views.ClassCategoryViewSet, basename='class-category')
router.register('descriptions', views.ClassDescriptionViewSet, basename='class-description')
router.register('schedules', views.ClassScheduleViewSet, basename='class-schedule')
router.register('instances', views.ClassInstanceViewSet, basename='class-instance')

urlpatterns = [
    path('', include(router.urls)),
]

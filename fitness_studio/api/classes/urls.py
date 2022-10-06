from rest_framework.routers import DefaultRouter

from api.classes import views

router = DefaultRouter()
router.register('classes/categories', views.ClassCategoryReadViewSet, basename='class-categories')
router.register('classes/descriptions', views.ClassDescriptionReadViewSet, basename='class-description')
router.register('classes/schedules', views.ClassScheduleReadViewSet, basename='class-schedule')
router.register('classes/instances', views.ClassInstanceReadViewSet, basename='class-instance')

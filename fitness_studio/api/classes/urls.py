from rest_framework.routers import DefaultRouter

from api.classes import views

router = DefaultRouter()
router.register('classes/categories', views.ClassCategoryViewSet, basename='class-categories')
router.register('classes/descriptions', views.ClassDescriptionViewSet, basename='class-description')
router.register('classes/schedules', views.ClassScheduleViewSet, basename='class-schedule')
router.register('classes/instances', views.ClassInstanceViewSet, basename='class-instance')

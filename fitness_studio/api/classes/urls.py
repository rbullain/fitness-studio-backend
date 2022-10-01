from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.classes import views

router = DefaultRouter()
router.register('categories', views.ClassCategoryReadViewSet, basename='class-categories')
router.register('descriptions', views.ClassDescriptionReadViewSet, basename='class-description')

urlpatterns = [
    path('', include(router.urls)),
]

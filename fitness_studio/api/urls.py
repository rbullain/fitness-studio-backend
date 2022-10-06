from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.classes.urls import router as classes_router
from api.locations.urls import router as locations_router

router = DefaultRouter()
router.registry.extend(classes_router.registry)
router.registry.extend(locations_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]

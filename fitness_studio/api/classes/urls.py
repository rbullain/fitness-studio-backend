from django.urls import path

from api.classes.views import (
    ClassCategoryListCreateView,
    ClassDescriptionListCreateView,
    ClassInstanceListCreateView,
    ClassScheduleListCreateView,
)

app_name = 'classes'

urlpatterns = [
    path('category', ClassCategoryListCreateView.as_view()),
    path('description', ClassDescriptionListCreateView.as_view()),
    path('instance', ClassInstanceListCreateView.as_view()),
    path('schedule', ClassScheduleListCreateView.as_view()),
]

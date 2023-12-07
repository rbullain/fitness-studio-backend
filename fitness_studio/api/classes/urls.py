from django.urls import path

from api.classes.views import ClassDescriptionListView, ClassScheduleListView, ClassInstanceListView, \
    ClassCategoryListView

app_name = 'classes'

urlpatterns = [
    path('description', ClassDescriptionListView.as_view()),
    path('schedule', ClassScheduleListView.as_view()),
    path('instance', ClassInstanceListView.as_view()),
    path('category', ClassCategoryListView.as_view()),
]

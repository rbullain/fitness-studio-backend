from django.urls import path

from apps.classes.views import ClassListView, ClassDetailView

urlpatterns = [
    path('', ClassListView.as_view()),
    path('<slug:slug>/', ClassDetailView.as_view()),
]

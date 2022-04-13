from django.urls import path

from apps.classes.views import ClassListView, ClassDetailView

app_name = 'classes'

urlpatterns = [
    path('', ClassListView.as_view(), name='class-list'),
    path('<slug:slug>/', ClassDetailView.as_view(), name='class-detail'),
]

from django.urls import path

from apps.classes.views import ClassDescriptionListView, ClassDescriptionDetailView, ClassBookingView

app_name = 'classes'

urlpatterns = [
    path('', ClassDescriptionListView.as_view(), name='class-list'),
    path('<slug:slug>/', ClassDescriptionDetailView.as_view(), name='class-detail'),
    path('<slug:cdslug>/<int:pk>/book/', ClassBookingView.as_view(), name='class-booking'),
]

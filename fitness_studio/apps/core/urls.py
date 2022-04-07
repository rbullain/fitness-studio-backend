from django.urls import path

from apps.core.views import HomePage

urlpatterns = [
    path('', HomePage.as_view()),
]

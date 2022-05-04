from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from apps.classes.models import ClassDescription, ClassInstance


class ClassDescriptionListView(ListView):
    model = ClassDescription
    template_name = 'classes/class-list.html'


class ClassDescriptionDetailView(DetailView):
    model = ClassDescription
    template_name = 'classes/class-detail.html'


class ClassBookingView(LoginRequiredMixin, DetailView):
    model = ClassInstance
    template_name = 'classes/class-booking.html'

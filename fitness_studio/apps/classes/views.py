from django.views.generic import DetailView, ListView

from apps.classes.models import ClassDescription


class ClassDetailView(DetailView):
    model = ClassDescription
    template_name = 'classes/class-detail.html'


class ClassListView(ListView):
    model = ClassDescription
    template_name = 'classes/class-list.html'

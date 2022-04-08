from django.views.generic import DetailView, ListView

from apps.classes.models import ClassDescription


class ClassDetailView(DetailView):
    model = ClassDescription
    template_name = 'class-detail.html'


class ClassListView(ListView):
    model = ClassDescription
    template_name = 'class-list.html'

from django.views.generic import CreateView, ListView, DetailView

from .services.ormutils import *
from .forms import *


class HomepageView(CreateView):
    form_class = AddPersonForm
    template_name = 'main/index.html'


class HellohumanspageView(ListView):
    model = Person
    template_name = 'main/hellohumanspage.html'
    context_object_name = 'humans'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = get_person_fields()

        return context


class HellopageView(DetailView):
    model = Person
    template_name='main/hellopage.html'
    pk_url_kwarg = "person_id"
    context_object_name = 'person'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_count'] = get_person_names_count(context['person'])

        return context





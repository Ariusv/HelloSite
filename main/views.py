from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

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
        context['columns'] = Person._meta.fields[1:]

        return context


class HellopageView(DetailView):
    model = Person
    template_name='main/hellopage.html'
    pk_url_kwarg = "person_id"
    context_object_name = 'person'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_count'] = Person.objects.filter(name=context['person'].name).count()

        return context





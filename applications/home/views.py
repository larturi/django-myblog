
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

from applications.entrada.models import Entry
from .forms import SubscribersForm, ContactForm
from .models import Home

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['portada'] = Entry.objects.entry_in_home()
        context['entradas_home'] = Entry.objects.entries_in_home()
        context['home'] = Home.objects.latest('created')
        context['entradas_recent'] = Entry.objects.entries_recent()
        context['form'] = SubscribersForm
        return context

class SuscriberCreateView(CreateView):
    form_class = SubscribersForm
    success_url = '.'

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
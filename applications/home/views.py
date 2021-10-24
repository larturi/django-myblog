
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView
)

from applications.entrada.models import Entry

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['portada'] = Entry.objects.entry_in_home()
        context['entradas_home'] = Entry.objects.entries_in_home()
        context['entradas_recent'] = Entry.objects.entries_recent()
        return context
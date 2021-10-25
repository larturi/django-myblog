from django.shortcuts import render

from django.views.generic import (
    ListView
)

from .models import Entry, Category

class EntryListView(ListView):
    template_name = 'entrada/lista.html'
    context_object_name = 'entradas'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        return context

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        category = self.request.GET.get('category', '')

        result = Entry.objects.buscar_entradas(kword, category)

        return result
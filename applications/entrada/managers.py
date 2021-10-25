from django.db import models

class EntryManager(models.Manager):

    def entry_in_home(self):
        return self.filter(
            public=True,
            portada=True
        ).order_by('-created').first()

    def entries_in_home(self):
        return self.filter(
            public=True,
            show_in_home=True
        ).order_by('-created')[:4]

    def entries_recent(self):
        return self.filter(
            public=True,
            portada=False
        ).order_by('-created')[:6]

    def buscar_entradas(self, kword, category):

        if len(category) > 0:
            return self.filter(
                category__short_name=category,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
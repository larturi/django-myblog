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
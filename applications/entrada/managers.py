from django.db import models

class EntryManager(models.Manager):

    def entry_in_home(self):
        return self.filter(
            public=True,
            portada=True
        ).order_by('-created').first()
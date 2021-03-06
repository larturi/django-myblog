from django.conf import settings
from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel
from applications.entrada.models import Entry
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()

    class Meta:
        unique_together = ['user', 'entry']
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    def __str__(self):
        return self.entry.title

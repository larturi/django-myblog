from django.contrib import admin

from .models import Favorites

class FavoritesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'entry',
    )

    search_fields = ('user', 'entry')
    list_filter = ('user',)


admin.site.register(Favorites, FavoritesAdmin)

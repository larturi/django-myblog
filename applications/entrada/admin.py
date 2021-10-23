from django.contrib import admin

from .models import Category, Tag, Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'category',
        'title',
        'public',
        'slug',
    )

    search_fields = ('user', 'slug')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'short_name',
        'name',
    )

    search_fields = ('name', 'short_name')
    list_filter = ('short_name',)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Entry, EntryAdmin)

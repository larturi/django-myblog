from django.contrib import admin

from .models import Home, Suscribers, Contact

class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'about_title',
        'about_text',
        'contact_email',
        'contact_phone',
    )

    search_fields = ('title', 'about_title')

class SuscribersAdmin(admin.ModelAdmin):
    list_display = (
        'email',
    )

    search_fields = ('email',)

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'message',
    )

    search_fields = ('full_name', 'message', )
    list_filter = ('email',)

admin.site.register(Home, HomeAdmin)
admin.site.register(Suscribers, SuscribersAdmin)
admin.site.register(Contact, ContactAdmin)


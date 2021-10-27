from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'full_name',
        'ocupation',
        'genero',
        'date_birth',
        'is_staff',
        'is_active',
    )

    search_fields = ('full_name', 'email')

admin.site.register(User, UserAdmin)

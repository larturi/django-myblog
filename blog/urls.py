"""
Proyecto Curso Django
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Internal Apps URLs
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),

    # URLs para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
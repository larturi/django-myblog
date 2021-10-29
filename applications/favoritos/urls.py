from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil', 
        views.UserPageView.as_view(),
        name='perfil',
    ),  
    path(
        'add-favorito/<pk>', 
        views.AddFavoritosView.as_view(),
        name='add-favorito',
    ),  
    path(
        'delete-favorito/<pk>', 
        views.DeleteFavoritosView.as_view(),
        name='delete-favorito',
    ),  
]
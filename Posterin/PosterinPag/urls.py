from django.urls import path
from .views import inicio, quienes, registro, novedades, inicio_sesion, perfil, edicion_perfil,editar_perfil
urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('quienes', quienes, name='quienes'),
    path('registro', registro, name='registro'),
    path('novedades', novedades, name='novedades'),
    path('iniciosesion', inicio_sesion, name='iniciosesion'),
    path('perfil', perfil, name='perfil'),
    path('edicionperfil', edicion_perfil, name='edicionperfil'),
    path('editar/', editar_perfil),
]
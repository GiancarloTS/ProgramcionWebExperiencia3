from django.urls import path
from .views import *
urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('quienes', quienes, name='quienes'),
    path('registro', registro, name='registro'),
    path('novedades', novedades, name='novedades'),
    path('galeria', tienda, name='galeria'),
    path('iniciosesion', inicio_sesion, name='iniciosesion'),
    path('pokemon',pokemon,name="pokemon"),
    path('contacto',contacto,name="contacto")

]
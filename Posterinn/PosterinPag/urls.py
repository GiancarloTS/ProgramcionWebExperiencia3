from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
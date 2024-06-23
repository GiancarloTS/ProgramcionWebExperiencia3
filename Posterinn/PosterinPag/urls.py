from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from PosterinPag import cart

from . import views


urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('quienes', views.quienes, name='quienes'),
    path('registro', views.registro, name='registro'),
    path('novedades', views.novedades, name='novedades'),
    path('tienda',views.listado_productos, name='tienda'),
    path('iniciosesion', views.inicio_sesion, name='iniciosesion'),
    path('pokemon',views.pokemon,name="pokemon"),
    path('contacto',views.contacto,name="contacto"),
    path('producto',views.producto,name="producto"),
    path('agregar/<id>',views.agregar,name="agregar"),
    path('reducir/<id>',views.reducir,name="reducir"),
    path('eliminar/<id>',views.eliminar,name="eliminar"),
    path('generarboleta/',views.generarboleta,name="generarboleta")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
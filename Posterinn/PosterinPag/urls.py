from django.contrib import admin
from django.urls import path



from PosterinPag import cart

from . import views 
from PosterinPag.views import * 


urlpatterns = [
    
  
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('eliminarproducto/<id>', eliminarproducto, name="eliminarproducto"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/',mostrar, name="mostrar"),
    
    path('adminproducto', views.productos, name='productos'),
    path('inicio', views.inicio, name='inicio'),
    path('quienes', views.quienes, name='quienes'),
    path('registro', views.registro, name='registro'),
    path('novedades', views.novedades, name='novedades'),
    path('tienda',views.listado_productos, name='tienda'),
    path('iniciosesion', views.inicio_sesion, name='iniciosesion'),

    path('perfil', perfil, name='perfil'),
    path('edicionperfil', edicion_perfil, name='edicionperfil'),
    path('editar/', editar_perfil),

    path('pokemon',views.pokemon,name="pokemon"),
    path('contacto',views.contacto,name="contacto"),
    path('producto',views.producto,name="producto"),
    path('agregar/<id>',views.agregar,name="agregar"),
    path('reducir/<id>',views.reducir,name="reducir"),
    path('eliminar/<id>',views.eliminar,name="eliminar"),
    path('generarboleta/',views.generarboleta,name="generarboleta")

]
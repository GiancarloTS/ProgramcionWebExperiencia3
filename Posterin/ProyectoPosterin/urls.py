"""
URL configuration for ProyectoPosterin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PosterinPag import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('PosterinPag.urls')),
    path('', views.inicio , name='inicio'),#CAMIAR CON EL INICIO DE YAN
    path('Registro/', views.registro, name='registro'),
    
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrarsesion'),
    path('inicio_sesion/', views.inicio_sesion, name='iniciosesion'),
    path('PerfilUsuario/', views.perfil, name='perfil'),
    path('EdicionPerfil/', views.edicion_perfil, name='edicionperfil'),
    path('editar/', views.editar_perfil, name='editar')
]

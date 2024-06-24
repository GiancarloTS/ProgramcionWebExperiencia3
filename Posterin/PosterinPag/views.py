from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuario, FormularioUsuario
# Create your views here.


def inicio(request):
    return render(request,'Inicio.html')

def quienes(request):
    return render(request,'QuienesSomos.html')

def novedades(request):
    return render(request,'Novedades.html')

@login_required
def perfil(request):
    return render(request, 'PerfilUsuario.html')


def registro(request):
    data={
        'form' : RegistroUsuario()
    }
    
    if request.method == 'GET':
        return render(request,'Registro.html', {
            'form' : RegistroUsuario
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            formulario = RegistroUsuario(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                user = authenticate(username=formulario.cleaned_data["username"], 
                password=formulario.cleaned_data["password1"])
                login(request, user)
                return redirect('tienda')
            data["form"]=formulario
        return render(request, 'Registro.html', data)
    
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'InicioSesion.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        
        if user is None: 
            return render(request, 'InicioSesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o clave incorrectas'
            })
        else:
            login(request, user)
            return redirect('tienda')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio') #CAMBIAR PARA QUE DIRIGA HACIA NUESTRO INICIO

@login_required
def edicion_perfil(request):
    user = request.user.id
    usuario = User.objects.get(id=user)
    return render(request, 'EdicionPerfil.html', {
        
        'user': usuario
    })

@login_required
def editar_perfil(request):
    nombre = request.POST['first_name']
    apellido = request.POST['last_name']

    user = request.user.id
    usuario = User.objects.get(id=user)
    
    usuario.first_name = nombre
    usuario.last_name = apellido

    usuario.save()
    return redirect('perfil')

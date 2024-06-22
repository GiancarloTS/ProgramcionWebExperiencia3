from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroUsuario
# Create your views here.


def pokemon(request):
    return render(request,'Pokemons.html')

def contacto(request):
    return render(request, 'Contactanos.html')


def inicio(request):
    return render(request,'Inicio.html')

def quienes(request):
    return render(request,'QuienesSomos.html')

def novedades(request):
    return render(request,'Novedades.html')

def tienda(request):
    return render(request, 'GaleriaDeFotos.html')

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
                '''user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'],
                last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password1'])'''
                login(request, user)
                return redirect('tienda')
            data["form"]=formulario
        return render(request, 'Registro.html', data)
      
    """ try:
        user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password1'])
        user.save()
        login(request, user)
        return redirect('tienda')
    except:
        return render(request, 'Registro.html', {
            'form': RegistroUsuario,
            "error": 'Este usuario ya existe'
        }) """ 
          
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

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio') #CAMBIAR PARA QUE DIRIGA HACIA NUESTRO INICIO






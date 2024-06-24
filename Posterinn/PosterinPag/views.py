from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ProductoForm, RegistroUsuario 
from django.contrib.auth.decorators import login_required
from .models import Producto
from . import cart
import datetime


# Create your views here.


# carrito de compra funciones
def productos(request):
    productos=Producto.objects.all() # select * from productos 
    context = {
            'productos' : productos
        }
    return render(request, 'producto/index.html',context)



@login_required
def crear(request):
    if request.method=="POST":
        productoform=ProductoForm(request.POST,request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert en función
            return redirect ('productos')
    else:
        productoform=ProductoForm()
    return render (request, 'Crear.html', {'productoform': productoform})
@login_required
def eliminarproducto(request, id): 
    productoEliminado = Producto.objects.get(codigo=id) #similar a select * from... where...
    productoEliminado.delete()
    return redirect ('productos')

@login_required
def modificar(request, id): 
    productoModificado = Producto.objects.get(codigo=id)  # Buscamos el objeto
    datos = {
        'form': ProductoForm(instance=productoModificado)
    }

    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos')

    return render(request, 'modificar.html', datos)

def registrar(request):
    data={                          #parámetro que llega al template
        'form': RegistroUsuario()
    }
    if request.method=="POST":
        formulario = RegistroUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()       #crear un objeto en el backend
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('index') 
        data["form"]=formulario           
    return render(request, 'registration/registrar.html',data)

def mostrar(request):
    autitos = Producto.objects.all()
    datos={
        'autitos':autitos
    }
    return render(request, 'mostrar.html', datos)


def listado_productos(request):
        productos=Producto.objects.all() # select * from productos 
        context = {
            'productos' : productos
        }
        return render(request, 'GaleriaDeFotos.html',context)

def agregar(request,id):
    carrito_compra= cart.carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.añadir_producto(producto=producto)
    return redirect('tienda')

def reducir(request, id):
        carrito_compra= cart.carrito(request)
        producto = Producto.objects.get(codigo=id)
        carrito_compra.quitar(producto=producto)
        return redirect('tienda')
def eliminar(request, id):
        carrito_compra= cart.carrito(request)
        producto = Producto.objects.get(codigo=id)
        carrito_compra.eliminar(producto=producto)
        return redirect('tienda')

def generarboleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
        boletaV = boleta(total = precio_total)
        boletaV.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(codigo = value['codigo'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id = boletaV, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boletaV.fechaCompra,
        'total': boletaV.total
    }
    request.session['boleta'] = boletaV.id
    carrito = cart.carrito(request)
    carrito.limpiar()
    return render(request, 'boleta.html',datos)
    # ----------------------------------------------------



def pokemon(request):
    return render(request,'Pokemons.html')

def contacto(request):
    return render(request, 'Contactanos.html')

def producto(request):
    return render(request,'Producto.html')

def inicio(request):
    return render(request,'Inicio.html')

def quienes(request):
    return render(request,'QuienesSomos.html')

def novedades(request):
    return render(request,'Novedades.html')


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





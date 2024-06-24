from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class RegistroUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username' : 'Usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Correo Electronico',
            'password1' : 'Contraseña',
            'password2' : 'Confirme Contraseña'
        }

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name']

        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['codigo', 'nombre', 'precio', 'descripcion', 'categoria', 'existencias', 'imagen']
        labels ={
            'codigo':'Codigo',
            'nombre' : 'Nombre',
            'precio': 'Precio',
            'descripcion': 'Descripcion',
            'categoria': 'Categoria',
            'existencias': 'Existencias',
            'imagen':'Imagen'
        }
        widgets={

            'codigo':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese codigo..',
                    'id': 'codigo',
                    'class': 'form-control',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre..',
                    'id':'nombre',
                    'class':'form-control',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'placeholder':'Ingrese precio..',
                    'id':'precio',
                    'class':'form-control',
                }
            ),

            'descripcion': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese descripcion..',
                    'id':'descripcion',
                    'class':'form-control',
                }
            ),
            
            'categoria': forms.Select(
                attrs={
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            
            'existencias': forms.NumberInput(
                attrs={
                    'id':'existencias',
                    'class':'form-control',
                }
            ),
            
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen',
                }
            )
        }
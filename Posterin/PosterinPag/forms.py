from django import forms
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



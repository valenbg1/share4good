from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuario(UserCreationForm):
    nombre = forms.CharField(required = True)
    apellidos = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    imagen = forms.URLField(required = False)
    telefono = forms.IntegerField(required = False)
    web = forms.CharField(required = False)
    descripcion = forms.TextField()
    
    

    

import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
       
class UserRegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    nombre = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Nombre"), error_messages={ 'invalid': _("This value must contain only letters") })
    apellidos = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=60)), label=_("Apellidos"))
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs=dict(required=True, max_length=9, min_value=0)), label=_("Telefono"))
    web = forms.CharField(widget=forms.TextInput(), label=_("Pagina web"))
    descripcion = forms.CharField(widget=forms.TextInput(), label=_("Descripcion"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
        
class OrganRegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    nombre = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Nombre"), error_messages={ 'invalid': _("This value must contain only letters") })
    direccion_fis = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=60)), label=_("Direccion fisica"))
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs=dict(required=True, max_length=9, min_value=0)), label=_("Telefono"))
    web = forms.CharField(widget=forms.TextInput(), label=_("Pagina web"))
    descripcion = forms.CharField(widget=forms.TextInput(), label=_("Descripcion"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

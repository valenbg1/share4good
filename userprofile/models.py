from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    imagen = models.URLField()
    telefono = models.IntegerField()
    web = models.CharField(max_length=60)
    descripcion = models.TextField()

class Organizacion(models.Model):
    nombre = models.CharField(max_length=30)
    logotipo = models.URLField()
    telefono = models.IntegerField()
    web = models.URLField()
    descripcion = models.TextField()
    direccionfis = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_usuario = models.ForeignKey(Usuario, null=True, related_name='log_info')
    is_organiz = models.ForeignKey(Organizacion, null=True, related_name='log_info')

class Inversion(models.Model):
    org = models.ForeignKey(Organizacion, related_name='inversiones')
    presupuesto = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.TextField()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

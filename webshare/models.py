from django.db import models

class Usuario(models.Model):
    uid = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField()
    imagen = models.URLField()
    telefono = models.IntegerField()
    web = models.CharField(max_length=60)
    descripcion = models.TextField()

class Organizacion(models.Model):
    uid = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    logotipo = models.URLField()
    telefono = models.IntegerField()
    web = models.URLField()
    descripcion = models.TextField()
    direccionfis = models.TextField()

class Inversion(models.Model):
    org = models.ForeignKey(Organizacion, related_name='inversiones')
    presupuesto = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.TextField()


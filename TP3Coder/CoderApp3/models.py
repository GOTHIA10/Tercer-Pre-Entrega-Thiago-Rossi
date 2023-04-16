from django.db import models
# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    numero = models.IntegerField()

class DT(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50)

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    SocioNro = models.IntegerField()
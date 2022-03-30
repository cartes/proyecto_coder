import email
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=55)
    apellidos = models.CharField(max_length=55)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=55)
    apellidos = models.CharField(max_length=55)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=55)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def curso(self):

    curso = Curso(nombre = "Web", camada = 1111)

    curso.save()

    documento = f"El curso es: {curso.nombre}, la camada es: {curso.camada}"

    return HttpResponse(documento)
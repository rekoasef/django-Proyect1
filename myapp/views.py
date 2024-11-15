from django.http import HttpResponse, JsonResponse
from .models import Proyect, task
from django.shortcuts import get_object_or_404

def Saludo(request):
    return HttpResponse("Hello World")

def otraRuta(request):
    return HttpResponse("<h1>Hola Soy un titulo</h1>")

def inicio(request):
    return HttpResponse("<h1>Bienvenido a la pagina principal</h1>")

def pidiendoParams(request, name):
    return HttpResponse(" Bienvenido %s" % name)

def proyectos(request):
    proyect = list(Proyect.objects.values()) #Guardamos los valores que habiamos puesto en la base de datos
    return JsonResponse(proyect, safe=False)

def Task(request, id):
    tarea = get_object_or_404(task, id = id)
    return HttpResponse("tarea: %s" % tarea.tittle)
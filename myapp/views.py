from django.http import HttpResponse, JsonResponse
from .models import Proyect, task
from django.shortcuts import get_object_or_404, render

def Saludo(request):
    return HttpResponse("Hello World")

def otraRuta(request):
    return HttpResponse("<h1>Hola Soy un titulo</h1>")

def inicio(request):
    username = "Renzo Asef"
    return render(request, "index.html", {
        'username': username
    })

def pidiendoParams(request, name):
    return HttpResponse(" Bienvenido %s" % name)

def proyectos(request):
    # proyect = list(Proyect.objects.values()) #Guardamos los valores que habiamos puesto en la base de datos
    proyectos = Proyect.objects.all()
    title = "Curso de Django"
    return render(request, "proyects.html", {
        "proyectos" : proyectos
    })

def Task(request):
    #tarea = get_object_or_404(task, id = id)
    tarea = task.objects.all()
    return render(request, "tasks.html", {
        'tarea': tarea
    })
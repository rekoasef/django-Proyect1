from django.http import HttpResponse

def Saludo(request):
    return HttpResponse("Hello World")

def otraRuta(request):
    return HttpResponse("<h1>Hola Soy un titulo</h1>")

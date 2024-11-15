from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.Saludo),
    path('tittle/', views.otraRuta),
    path('home/', views.inicio),
    path('saludoNombre/<str:name>', views.pidiendoParams)
]

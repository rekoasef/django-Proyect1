from django.urls import path
from . import views

urlpatterns = [
    path('saludo', views.Saludo),
    path('tittle/', views.otraRuta),
    path('/home', views.inicio)
]

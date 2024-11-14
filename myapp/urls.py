from django.urls import path
from . import views

urlpatterns = [
    path('', views.Saludo),
    path('tittle/', views.otraRuta)
]

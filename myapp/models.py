from django.db import models

# Create your models here.

class Proyect(models.Model):
    name = models.CharField(max_length=50)
    
class task(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE)#El foreingkey es para decir que este campo tiene relacion con otra tabla
    
class Description(models.Model):
    text = models.TextField()
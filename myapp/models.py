from django.db import models

# Create your models here.

class Proyect(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class task(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE)#El foreingkey es para decir que este campo tiene relacion con otra tabla
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tittle + ' - ' + self.proyect.name
    
class Description(models.Model):
    text = models.TextField()
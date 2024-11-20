from django import forms

class CreateNewTask(forms.Form):
    tittle = forms.CharField(label="Titulo de Tarea", max_length=200)
    description = forms.CharField(label= "Descripcion de la Tarea", widget=forms.Textarea)
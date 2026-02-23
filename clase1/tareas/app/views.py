from django.shortcuts import render
from .models import Tarea

# Create your views here.

def lista_tareas(request):
    tareas = Tarea.objects.all() # ORM ->  SELECT * FROM TAREA
    return render(request, 'lista_tareas.html', {"tareas":tareas})

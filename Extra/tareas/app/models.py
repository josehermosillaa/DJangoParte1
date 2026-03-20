from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    
    """
    pendiente, en progreso y completada

    """
    STATUS_CHOICES = [
            ('P', 'Pendiente'),
            ('E', 'En progreso'),
            ('C', 'Completada')
    ]

    
    title = models.CharField(verbose_name='Titulo',max_length = 100)
    description = models.TextField(verbose_name='Descripción',blank = True)
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Asignado a')
    status = models.CharField(verbose_name='Estado',max_length=1, choices=STATUS_CHOICES, default='P' )
    created_at = models.DateTimeField(verbose_name='Fecha de Creación',auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
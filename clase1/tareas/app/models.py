from django.db import models

# Create your models here.

class Tarea(models.Model):

    titulo = models.CharField(max_length=100) # VARCHAR(100) MySQL
    descripcion = models.TextField(blank=True) # TEXT() permite texto variable depende de la memoria del sistema
    

    def __str__(self):
        return self.titulo
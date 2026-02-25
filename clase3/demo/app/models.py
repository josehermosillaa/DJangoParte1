from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=120) # VARCHAR(100)
    descripcion = models.TextField(blank = True) #TEXT
    precio =  models.DecimalField(max_digits=9,decimal_places=2) #DECIMAL(10,2)
    imagen_url = models.URLField(max_length=200, blank=True, null=True)
    

    #metodo que permite configurar como se ven las instancias de una clase 
    def __str__(self):
        return f"{self.nombre} Precio: {self.precio}"
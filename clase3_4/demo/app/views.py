from django.shortcuts import render
#importamos el modelo de donde queremos sacar los datos
from .models import Producto
import random
# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all() #SELECT * FROM Producto / con el ORM de DJANGO
    return render(request, 'lista_productos.html', {'productos':productos})
    #                              key para leer los datos en el html: los datos obtenidos


def home(request):
    productos = Producto.objects.all() #
    seleccion_aleatoria = random.sample(list(productos),3) #objetos de productos
    # imagenes = [producto.imagen_url for producto in seleccion_aleatoria]
    imagenes = []
    for producto in seleccion_aleatoria:
        imagenes.append(producto.imagen_url)


    return render(request, 'base.html',{'imagenes':imagenes})
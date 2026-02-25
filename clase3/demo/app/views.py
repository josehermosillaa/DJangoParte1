from django.shortcuts import render
#importamos el modelo de donde queremos sacar los datos
from .models import Producto
# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all() #SELECT * FROM Producto / con el ORM de DJANGO
    return render(request, 'lista_productos.html', {'productos':productos})
    #                              key para leer los datos en el html: los datos obtenidos
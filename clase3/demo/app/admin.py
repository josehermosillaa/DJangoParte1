from django.contrib import admin
## debo importar mis modelos desde model.py
from .models import Producto

# Register your models here.
#para registrar un modelo en el panel de administrador

admin.site.register(Producto)
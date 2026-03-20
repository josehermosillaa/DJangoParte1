from django.contrib import admin
## debo importar mis modelos desde model.py
from .models import Producto, Usuario

# Register your models here.
#para registrar un modelo en el panel de administrador

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio') #campos que quiero mostrar en el panel de admin
    search_fields = ('nombre',) #campos por los que quiero buscar en el panel de admin
    list_filter = ('precio',) #campos por los que quiero filtrar en el panel de admin


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario)
admin.site.site_header = "Panel de Administración BOOTCAMP"
admin.site.site_title = "Administración BOOTCAMP"
admin.site.index_title = "Bienvenido al panel de administración del BOOTCAMP"
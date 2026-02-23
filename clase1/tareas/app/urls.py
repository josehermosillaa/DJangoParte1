from django.contrib import admin
from django.urls import path
from .views import lista_tareas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_tareas, name='lista_tareas'),
]

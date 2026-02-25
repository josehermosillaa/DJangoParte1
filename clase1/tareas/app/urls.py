from django.contrib import admin
from django.urls import path
from .views import lista_tareas
urlpatterns = [

    path('', lista_tareas, name='lista_tareas'),
    # path('1/', lista_tareas, name='lista_tareas'),
]

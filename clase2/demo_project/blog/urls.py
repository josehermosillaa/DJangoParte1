

from django.urls import path
from .views import hola_mundo, datos
urlpatterns = [     
    path('hola/', hola_mundo, name="hola mundo" ),
    path('datos/', view=datos, name="datos" ),
]

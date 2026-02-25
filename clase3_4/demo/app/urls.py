from django.urls import path
from .views import lista_productos, home


urlpatterns = [
    path('',lista_productos, name='lista_productos' ),
    path('inicio/',home, name='pagina_inicio' ),
]

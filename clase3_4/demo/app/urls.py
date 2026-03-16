from django.urls import path
from .views import lista_productos, home, prueba, ejemplo_error, formulario_test
from django.conf.urls import handler404

urlpatterns = [
    path('',lista_productos, name='lista_productos' ),
    path('inicio/',home, name='pagina_inicio' ),
    path('prueba/',prueba, name='prueba' ),
    path("test/",ejemplo_error, name="ejemplo"),
    path("formulario/",formulario_test, name="formulario")

    
]

handler404 = 'app.views.error_404'
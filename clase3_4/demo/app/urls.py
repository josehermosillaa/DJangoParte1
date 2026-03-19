from django.urls import path
from .views import lista_productos, home, prueba, ejemplo_error, formulario_test, usuario_form_view, DashboardView,VistaProtegida
from django.conf.urls import handler404

urlpatterns = [
    path('',lista_productos, name='lista_productos' ),
    path('inicio/',home, name='pagina_inicio' ),
    path('prueba/',prueba, name='prueba' ),
    path("test/",ejemplo_error, name="ejemplo"),
    path("formulario/",formulario_test, name="formulario"),
    path("registro/",usuario_form_view, name="usuario_form"),
    path("dashboard/",DashboardView.as_view(), name="dashboard"),
    path('protegida/',VistaProtegida.as_view(), name='protegida')
]

handler404 = 'app.views.error_404'
handler403 = 'app.views.error_403'
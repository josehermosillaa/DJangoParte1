from django.shortcuts import render, redirect
from django.http import HttpResponse
#importamos el modelo de donde queremos sacar los datos
from .models import Producto, Usuario
import random

#importacion para el formulario
from .forms import NombreForm, ProductoForm, UsuarioForm, RegisterForm
from django.contrib import messages
# Create your views here.

#
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, View

from django.core.exceptions import PermissionDenied
#esto se utiliza para trabajar en las vistas basadas en CLASES  

from django.contrib.auth.decorators import login_required, permission_required

#autologin
from django.contrib.auth import login

@login_required
def lista_productos(request):
    productos = Producto.objects.all() #SELECT * FROM Producto / con el ORM de DJANGO
    return render(request, 'lista_productos.html', {'productos':productos})
    #                              key para leer los datos en el html: los datos obtenidos

@login_required
def home(request):
    productos = Producto.objects.all() #
    seleccion_aleatoria = random.sample(list(productos),3) #objetos de productos
    # imagenes = [producto.imagen_url for producto in seleccion_aleatoria]
    imagenes = []
    for producto in seleccion_aleatoria:
        imagenes.append(producto.imagen_url)


    return render(request, 'base.html',{'imagenes':imagenes, 'login':False, 'username':"Elba lazo"})

@login_required
def prueba(request):
    items = ['Banana','Platano','Durazno', 'Naranja']
    
    return render(request, 'prueba.html', context={'frutas':items})
    
    #{{frutas}}
    
def error_404(request):
    return render(request, '404.html', status=404)

def ejemplo_error(request):
    try:
        x = 1/0 #lanza error
        return HttpResponse(f"Resultado: {x}")
    except ZeroDivisionError:
        return HttpResponse("Ocurrio un error: division por cero", status = 400)
    

###### vista para formulario
@login_required
@permission_required('app.change_usuario', raise_exception=True)
def formulario_test(request):

    if request.method == 'POST':
        form = NombreForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['contrasena']

            return render(request,'resultado.html',context = {'nombre':nombre,'email':email, 'contrasena':contrasena})

    else: #metodo GET 
        form = NombreForm()
    return render(request, 'formulario.html', context = {'form':form})

def usuario_form_view(request):
    if request.user.has_perm('app.change_usuario'):
        usuarios = Usuario.objects.all()


        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                form.save() #esto se permite ya que estamos usando un modelo de la base de datos con  MODELFORM
                messages.success(request, 'Usuario registrado correctamente.')
                return redirect('usuario_form')
            else:
                messages.error(request, 'Corrijan los errores en el formulario')
        else: #metodo GET 
            form = UsuarioForm()
        
        return render(request, 'usuario_form.html', context = {'form':form, 'usuarios':usuarios})
            
        
    else:
        raise PermissionDenied


class DashboardView(LoginRequiredMixin,PermissionRequiredMixin ,TemplateView):
    template_name = 'dashboard.html'
    permission_required = 'app.change_producto'

    
class VistaProtegida(PermissionRequiredMixin, View):
    permission_required = 'app.change_usuario'
    
    def get(self, request):
            return HttpResponse("Acceso permitido")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #guardar los datos en el modelo en que se enlaza el formulario
            login(request, user)
            return redirect('pagina_inicio') #o donde queramos
    else:
        form = RegisterForm()
    
    return render(request, "register.html",{"form":form})
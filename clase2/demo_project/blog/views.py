from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola_mundo(request):
    return HttpResponse("Hola como estan!")

def datos(request):
    return render(request, 'index.html',{'nombres':["juanito", "diego", "fabian"]})
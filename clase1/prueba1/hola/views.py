from django.http import HttpResponse

# Create your views here.

def hola_mundo(request):
    
    return HttpResponse("Hola Mundo desde Django")
#herramienta para formularios en Django
from django import forms

class NombreForm(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=20, error_messages={'max_length':'nombre muy largo'})
    email = forms.EmailField(label='Correo label')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
#herramienta para formularios en Django
from django import forms


from .models import Producto, Usuario

class NombreForm(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=20, error_messages={'max_length':'nombre muy largo'})
    email = forms.EmailField(label='Correo label',error_messages={'invalid':'Correo No valido'})
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


###ejemplo con el modelo Producto
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'  

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'edad']

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'edad': forms.NumberInput(attrs={'class':'form-control','type':"text", 'placeholder':"Disabled input", 'aria-label':"Disabled input example"})
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre.lower() == 'admin': #lower deja todo el texto en minusculas
            raise forms.ValidationError('No se permite el nombre admin')
        return nombre
    
    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 0:
            raise forms.ValidationError('Edad debe ser un valor valido (positivo)')
        return edad
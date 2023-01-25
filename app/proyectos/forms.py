from django import forms

#Modelo
from app.proyectos.models import Contactar

class ContactarForm(forms.ModelForm):
    class Meta: 
        model = Contactar

        fields = ['nombre', 'correo', 'proyecto', 'mensaje']

        labels = {
            'nombre' : 'Nombre :',
            'correo' : 'Correo :',
            'proyecto' : 'Proyecto :',
            'mensaje' : 'Mensaje'
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'correo' : forms.EmailInput(attrs={'class':'form-control'}),
            'proyecto' : forms.TextInput(attrs={'class':'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class':'form-control'})
        }


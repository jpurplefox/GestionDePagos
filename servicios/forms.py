from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('descripcion', 'se_cobra_por_hora')
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'se_cobra_por_hora': forms.CheckboxInput(attrs={'class': ''})
        }

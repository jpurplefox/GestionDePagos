from django import forms
from .models import Marca, Modelo

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ('nombre',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
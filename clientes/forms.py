from django import forms
from .models import Cliente, Vehiculo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'dni', 'email', 'observaciones')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('modelo', 'year', 'patente')
        widgets = {
            'modelo': forms.Select(attrs={'class': 'form-control chosen-select', 'data-placeholder': 'Elija un modelo', 'tabindex': '2'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
        }


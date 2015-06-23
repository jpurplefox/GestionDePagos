from django import forms
from .models import Cliente, Vehiculo
from vehiculos.models import Marca, Modelo

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

def get_modelos_list(modelos):
    return [(modelo.id, modelo.nombre) for modelo in modelos]

def get_modelo_choices():
    choices = [(marca.nombre, get_modelos_list(marca.modelos.all())) for marca in Marca.objects.all()]
    choices.insert(0, ('', '-----'))
    return choices

class VehiculoForm(forms.ModelForm):
    modelo = forms.ChoiceField(label='Modelo', widget=forms.Select(attrs={'class': 'form-control chosen-select'}), choices=get_modelo_choices())
    class Meta:
        model = Vehiculo
        fields = ('modelo', 'year', 'patente')
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_modelo(self):
        modelo_pk = self.cleaned_data['modelo']
        modelo = Modelo.objects.get(id=modelo_pk)
        return modelo
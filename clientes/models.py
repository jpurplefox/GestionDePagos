from django.db import models
from django.core.urlresolvers import reverse
from vehiculos.models import Modelo
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='DNI')
    email = models.EmailField()
    observaciones = models.TextField()
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre', 'apellido']

    def __str__(self):
        nombre = '{nombre} {apellido}'.format(nombre=self.nombre, apellido=self.apellido)
        if not self.activo:
            nombre += ' (Inactivo)'
        return nombre

    def get_absolute_url(self):
        return reverse('clientes:cliente_detail', args=[self.id])

    def delete(self):
        self.activo = False
        for vehiculo in self.vehiculos.all():
            vehiculo.delete()
        self.save()

class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='vehiculos')
    modelo = models.ForeignKey(Modelo, related_name='vehiculos')
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Año')
    patente = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]{3}[0-9]{3}$',
                message='La patente debe tener tres letras seguidas de tres numeros. Ejemplo "ABC123"',
                code='invalid_patente'
            ),
        ]
    )
    foto = models.ImageField(upload_to="vehiculos/fotos", null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        nombre = '{modelo} - {patente}'.format(modelo=self.modelo.nombre, patente=self.patente.upper())
        if not self.activo:
            nombre += ' (Inactivo)'
        return nombre

    def get_absolute_url(self):
        return reverse('clientes:vehiculo_detail', args=[self.id])

    def delete(self):
        self.activo = False
        self.save()
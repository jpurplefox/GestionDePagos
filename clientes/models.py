from django.db import models
from django.core.urlresolvers import reverse
from vehiculos.models import Modelo

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='DNI')
    email = models.EmailField()
    observaciones = models.TextField()

    class Meta:
        ordering = ['nombre', 'apellido']

    def __str__(self):
        return '{nombre} {apellido}'.format(nombre=self.nombre, apellido=self.apellido)

    def get_absolute_url(self):
        return reverse('clientes:cliente_detail', args=[self.id])

class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='vehiculos')
    modelo = models.ForeignKey(Modelo, related_name='vehiculos')
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Año')
    patente = models.CharField(
        max_length=6
    )
    foto = models.ImageField(upload_to="vehiculos/fotos", null=True, blank=True)

    def __str__(self):
        return '{modelo} ({patente})'.format(modelo=self.modelo.nombre, patente=self.patente)

    def get_absolute_url(self):
        return reverse('clientes:vehiculo_detail', args=[self.id])

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='DNI', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=25, verbose_name='Teléfono', blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
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

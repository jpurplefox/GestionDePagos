from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('vehiculos:marca_detail', args=[self.id])

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, related_name='modelos')

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return '{modelo} ( {marca} )'.format(modelo=self.nombre, marca=self.marca.nombre)

    def get_absolute_url(self):
        return reverse('vehiculos:modelo_detail', args=[self.id])
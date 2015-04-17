from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	dni = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='DNI')
	email = models.EmailField()
	observaciones = models.TextField()

	def __str__(self):
		return '{nombre} {apellido}'.format(nombre=self.nombre, apellido=self.apellido)

	def get_absolute_url(self):
		return reverse('clientes:cliente_detail', args=[self.id])

	class Meta:
		ordering = ['nombre', 'apellido']
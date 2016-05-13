from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Servicio(models.Model):
    descripcion = models.CharField(max_length=200)
    se_cobra_por_hora = models.BooleanField(verbose_name='se cobra por hora')
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['descripcion']

    def __str__(self):
        nombre = '{descripcion}'.format(descripcion=self.descripcion)
        if not self.activo:
            nombre += ' (Inactivo)'
        return nombre

    def get_absolute_url(self):
        return reverse('servicios:servicio_detail', args=[self.id])

    def delete(self):
        self.activo = False

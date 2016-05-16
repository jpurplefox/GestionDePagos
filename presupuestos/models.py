from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Presupuesto(models.Model):
    fecha = models.DateField()
    validez = models.DateField()
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return 'N° {numero}'.format(numero=self.id)

    def get_absolute_url(self):
        return reverse('presupuestos:detail', args=[self.id])

class PresupuestoDetalle(models.Model):
    presupuesto = models.ForeignKey('Presupuesto', on_delete=models.CASCADE, related_name='detalles')
    servicio = models.ForeignKey('servicios.Servicio', on_delete=models.PROTECT, related_name='+')
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    #Para servicios que se cobran por hora
    horas = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cobra_en_sesion = models.BooleanField(default=False)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_modelo'),
        ('clientes', '0002_auto_20150421_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('year', models.DecimalField(max_digits=4, verbose_name='Año', decimal_places=0)),
                ('patente', models.CharField(max_length=6)),
                ('foto', models.ImageField(upload_to='vehiculos/fotos', blank=True, null=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente', related_name='vehiculos')),
                ('modelo', models.ForeignKey(to='vehiculos.Modelo', related_name='vehiculos')),
            ],
        ),
    ]

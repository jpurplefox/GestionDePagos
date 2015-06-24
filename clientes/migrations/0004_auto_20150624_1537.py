# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='patente',
            field=models.CharField(validators=[django.core.validators.RegexValidator(code='invalid_patente', regex='^[a-zA-Z]{3}[0-9]{3}$', message='La patente debe tener tres letras seguidas de tres numeros. Ejemplo "ABC123"')], max_length=6),
        ),
    ]

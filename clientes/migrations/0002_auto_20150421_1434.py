# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nombre', 'apellido']},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.DecimalField(verbose_name='DNI', max_digits=8, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'ordering': ['descripcion']},
        ),
        migrations.AddField(
            model_name='servicio',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]

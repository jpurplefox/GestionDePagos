# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.DecimalField(max_digits=8, decimal_places=0)),
                ('email', models.EmailField(max_length=75)),
                ('observaciones', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-10 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0005_auto_20180507_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paresporpunto',
            name='linea',
        ),
        migrations.DeleteModel(
            name='ParesPorPunto',
        ),
    ]

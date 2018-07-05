# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-19 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20180613_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='descripcion',
            field=models.TextField(blank=True, max_length=600, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='numero',
            field=models.IntegerField(default=0, verbose_name='N\xfamero de Lote'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='observaciones',
            field=models.CharField(blank=True, max_length=600, verbose_name='Observaciones'),
        ),
    ]
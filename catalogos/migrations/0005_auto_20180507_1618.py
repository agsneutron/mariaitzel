# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-07 16:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_merge_20180507_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='calle',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Este campo no debe contener numeros', regex='^[a-zA-Z ]*$')], verbose_name='Calle'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='colonia',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Este campo no debe contener numeros', regex='^[a-zA-Z ]*$')], verbose_name='Colonia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Este campo no debe contener numeros', regex='^[a-zA-Z ]*$')], verbose_name='Nombre'),
        ),
    ]

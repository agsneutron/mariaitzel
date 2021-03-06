# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-10 20:38
from __future__ import unicode_literals

import concurrency.fields
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
                'verbose_name': 'Pa\xeds',
                'verbose_name_plural': 'Pa\xedses',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.IntegerVersionField(default=0, help_text='record revision number')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('calle', models.CharField(max_length=50, verbose_name='Calle')),
                ('numero', models.CharField(max_length=10, verbose_name='N\xfamero')),
                ('colonia', models.CharField(max_length=50, verbose_name='Colonia')),
                ('cp', models.CharField(max_length=20, verbose_name='C.P.')),
                ('telefono', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tel\xe9fono')),
                ('telefono_dos', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tel\xe9fono No.2')),
                ('email', models.CharField(max_length=60, verbose_name='Correo Electr\xf3nico')),
                ('rfc', models.CharField(max_length=20, verbose_name='RFC')),
                ('last_edit_date', models.DateTimeField(auto_now_add=True)),
                ('estado', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='pais', chained_model_field='pais', on_delete=django.db.models.deletion.CASCADE, to='catalogos.Estado')),
                ('municipio', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='estado', chained_model_field='estado', on_delete=django.db.models.deletion.CASCADE, to='catalogos.Municipio')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Pais', verbose_name='Pa\xeds')),
            ],
            options={
                'verbose_name_plural': 'Proveedor',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Pais'),
        ),
    ]

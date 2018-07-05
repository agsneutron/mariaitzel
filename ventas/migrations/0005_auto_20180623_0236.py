# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-23 02:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20180622_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedido',
            name='usuario_genera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detallepedido_requests_created', to=settings.AUTH_USER_MODEL, verbose_name='Usuario que Genera'),
        ),
    ]

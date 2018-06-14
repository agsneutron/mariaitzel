# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0005_auto_20171104_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcionordencompra',
            name='detalleordencopra',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='almacen.DetalleOrdenCompra', verbose_name='Detalle Orden de Compra'),
            preserve_default=False,
        ),
    ]

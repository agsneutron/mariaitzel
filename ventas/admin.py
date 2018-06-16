# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Lote, ParesPorPunto, Pedido,ParesPorPuntoPedido,DetallePedido
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from forms import DetallePedidoForm

# Register your models here.


# Administrador para el catálogo de Proveedores


class ParesPorPuntoInlines(admin.TabularInline):
    model = ParesPorPunto
    extra = 1
    fields = ('talla','total_pares',)

    def get_extra(self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra

    def get_formset(self, request, obj=None, **kwargs):
        ## Put in your condition here and assign extra accordingly
        if obj is None:
            return super(ParesPorPuntoInlines, self).get_formset(request, obj, **kwargs)
        topic_images = 'NO'

        kwargs['extra'] = 0
        if len(topic_images) <= 3:
            kwargs['extra'] = 10 - len(topic_images)
        return super(ParesPorPuntoInlines, self).get_formset(request, obj, **kwargs)


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    inlines = [ParesPorPuntoInlines,]
    model = Lote
    exclude = None

class ParesPorPuntoPedidoInlines(NestedStackedInline):
    model = ParesPorPuntoPedido
    extra = 1
    fields = ('talla','total_pares',)



class DetallePedidoInlines(NestedStackedInline):
    model = DetallePedido
    inlines = [ParesPorPuntoPedidoInlines, ]
    form = DetallePedidoForm
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(NestedModelAdmin):
    inlines = [DetallePedidoInlines,]
    model = Pedido
    fields = ('folio', 'cliente', 'fecha_creacion', 'observaciones')
    exclude = None
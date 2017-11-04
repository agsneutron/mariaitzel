# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import CategoriaArticulo,Articulo,OrdenCompra,DetalleOrdenCompra,UnidadMedida

# Register your models here.

# Administrador para el catálogo de CategoriaArticulo
class CategoriaArticuloAdmin(admin.ModelAdmin):
    model = CategoriaArticulo
    fields = ('nombre',)

# Administrador para el catálogo de CategoriaArticulo
class ArticuloAdmin(admin.ModelAdmin):
    model = Articulo
    fieldsets = (
        ('Articulos',{
            'classes': ('wrap',),
            'fields':('categoria','clave','nombre','cantidad','unidad_medida','precio','stock_minimo',)
        }),
    )

#Administrador para la Orden de Compra
class DetalleOrdenCompraInline(admin.TabularInline):
    fields = ('articulo','cantidad_pedida','costo_compra','iva','unidad_medida_compra','descripcion')
    model = DetalleOrdenCompra


class OrdenCompraAdmin(admin.ModelAdmin):
    model = OrdenCompra
    list_display = ('folio','fecha_oc','proveedor','fecha_entrega')
    inlines = (DetalleOrdenCompraInline,)


admin.site.register(CategoriaArticulo)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(OrdenCompra,OrdenCompraAdmin)
admin.site.register(UnidadMedida)
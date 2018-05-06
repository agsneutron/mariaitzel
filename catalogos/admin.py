# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Proveedor, Pais, Estado, Municipio,DireccionEntrega, Cliente

# Register your models here.


# Administrador para el catálogo de Proveedores

class ProveedorAdmin(admin.ModelAdmin):
     list_display = ('id', 'nombre', 'rfc', 'email', 'estado', 'municipio')
     search_fields = ('nombre', 'rfc', 'estado__nombre', 'email', 'municipio__nombre')
     list_display_links = ('id', 'nombre', 'rfc')
     list_per_page = 50

     def get_fields(self, request, obj=None):
         fields = (
             'nombre', 'rfc', 'email', 'telefono', 'telefono_dos', 'pais', 'estado', 'municipio', 'cp',
             'calle',
             'numero', 'colonia')
         return fields

class DireccionEntregaInlines(admin.TabularInline):
    model = DireccionEntrega
    extra = 1
    fields = ('pais','estado','municipio','calle', 'numero', 'colonia', 'cp','telefono',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [DireccionEntregaInlines,]
    exclude = None

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Proveedor, ProveedorAdmin)
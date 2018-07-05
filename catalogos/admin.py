# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Proveedor, Pais, Estado, Municipio,DireccionEntrega, Cliente,Corte, Forro, Ojillo, Agujeta, Suela, Linea, Estilo, Color

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
            return super(DireccionEntregaInlines, self).get_formset(request, obj, **kwargs)
        topic_images = 'NO'

        kwargs['extra'] = 0
        #if len(topic_images) <= 3:
        #    kwargs['extra'] = 10 - len(topic_images)
        return super(DireccionEntregaInlines, self).get_formset(request, obj, **kwargs)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [DireccionEntregaInlines,]
    exclude = None


admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Corte)
admin.site.register(Forro)
admin.site.register(Ojillo)
admin.site.register(Agujeta)
admin.site.register(Suela)
admin.site.register(Linea)
admin.site.register(Estilo)
admin.site.register(Color)
#admin.site.register()
admin.site.register(Proveedor, ProveedorAdmin)
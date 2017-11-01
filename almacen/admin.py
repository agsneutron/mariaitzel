# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import CategoriaArticulo,Articulo

# Register your models here.

# Administrador para el catálogo de CategoriaArticulo
class CategoriaArticuloAdmin(admin.ModelAdmin):
    model = CategoriaArticulo
    fields = ('nombre',)

# Administrador para el catálogo de CategoriaArticulo
class ArticuloAdmin(admin.ModelAdmin):
    model = Articulo
    fields = ('categoria','clave','nombre','cantidad','unidad_medida','precio','stock_minimo',)

admin.site.register(CategoriaArticulo)
admin.site.register(Articulo, ArticuloAdmin)
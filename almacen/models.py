# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.forms.models import model_to_dict

# Create your models here.

@python_2_unicode_compatible
class UnidadMedida(models.Model):
    nombre = models.CharField(verbose_name="Unidad de Medida", max_length=50, null=False, blank=False,
                              unique=True)
    abreviatura = models.CharField(verbose_name="Unidad de Medida Abreviado", max_length=50, null=False, blank=False,
                              unique=True)

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        return dict

    def __str__(self):
        return self.abreviatura

    def __unicode__(self):
        return self.abreviatura

@python_2_unicode_compatible
class CategoriaArticulo(models.Model):
    nombre = models.CharField(verbose_name="Nombre de la Categoría", max_length=50, null=False, blank=False,
                              unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

@python_2_unicode_compatible
class EstatusArticulo(models.Model):
    nombre = models.CharField(verbose_name="Estatus", max_length=50, null=False, blank=False,
                              unique=True)

    class Meta:
        verbose_name = "Estatus"
        verbose_name_plural = "Estatus"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['id'] = str(self.id)
        return dict

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

class Articulo(models.Model):
    clave = models.CharField(verbose_name="Clave del Artículo", max_length=20, null=False, blank=False, unique=True,default="")
    categoria = models.ForeignKey(CategoriaArticulo, null=False, blank=False, verbose_name="Categoría")
    nombre = models.CharField(verbose_name="Nombre del artículo", max_length=150, null=False, blank=False,
                              unique=True)
    cantidad = models.FloatField(verbose_name="Cantidad", default=0, blank=True, null=True, )
    unidad_medida = models.ForeignKey(UnidadMedida, null=False, blank=False, verbose_name="Unidad de Medida")
    precio = models.DecimalField(verbose_name='Precio', decimal_places=2, blank=True, null=True,
                                       default=0, max_digits=20)
    stock_minimo = models.FloatField(verbose_name="Stock Mínimo", default=0, blank=True, null=True, )
    estatus = models.ForeignKey(EstatusArticulo, null=False, blank=False, verbose_name="Estatus")




    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['categoria'] = self.categoria.nombre
        dict['id'] = str(self.id)
        return dict

    def __str__(self):
        return self.categoria.nombre + ": " + self.nombre

    def __unicode__(self):
        return self.categoria.nombre + ": " + self.nombre

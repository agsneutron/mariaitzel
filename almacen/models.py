# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.forms.models import model_to_dict
from catalogos.models import Proveedor
from users.models import User

# Create your models here.

@python_2_unicode_compatible
class UnidadMedida(models.Model):
    nombre = models.CharField(verbose_name="Unidad de Medida", max_length=50, null=False, blank=False,
                              unique=True)
    numero_unidades = models.CommaSeparatedIntegerField(verbose_name='Número de Unidades', default=0, null=False, blank=False, editable=True, max_length=20)
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
    nombre = models.CharField(verbose_name="Nombre del Artículo", max_length=150, null=False, blank=False,
                              unique=True)
    cantidad = models.FloatField(verbose_name="Cantidad", default=0, blank=True, null=True, )
    unidad_medida = models.ForeignKey(UnidadMedida, null=False, blank=False, verbose_name="Unidad de Medida")
    precio = models.DecimalField(verbose_name='Precio', decimal_places=2, blank=True, null=True,
                                       default=0, max_digits=20)
    stock_minimo = models.FloatField(verbose_name="Stock Mínimo", default=0, blank=True, null=True, )
    estatus = models.ForeignKey(EstatusArticulo, null=True, blank=True, verbose_name="Estatus")

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

class OrdenCompra(models.Model):
    folio = models.CharField(verbose_name="Fólio", max_length=30, null=False, blank=False, unique=True,default="",)
    proveedor = models.ForeignKey(Proveedor, null=False, blank=False, verbose_name="Proveedor")
    fecha_oc = models.DateField(verbose_name="Fecha de Orden de Compra", null=False, blank=False,)
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega", blank=True, null=True, )
    factura = models.CharField(max_length=50, null=False, blank=False, verbose_name="Factura")
    lugar_entrega = models.CharField(verbose_name='Lugar de Entrega', blank=True, null=True, max_length=250)
    usuario_genera = models.ForeignKey(User, verbose_name="Usuario que Genera", blank=True, null=False, related_name='%(class)s_requests_created')
    usuario_recibe = models.ForeignKey(User, null=True, blank=False, verbose_name="Usuario que Recibe", related_name='%(class)s_requests_modifies')

    class Meta:
        verbose_name = "Orden de Compra"
        verbose_name_plural = "Orden de Compra"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['proveedor'] = self.proveedor.nombre
        dict['usuario_genera'] = self.usuario_genera.username
        dict['usuario_recibe'] = self.usuario_recibe.username
        dict['id'] = str(self.id)
        return dict

    def __str__(self):
        return self.folio + ": " + self.folio

    def __unicode__(self):
        return self.folio + ": " + self.folio


class DetalleOrdenCompra(models.Model):
    ordencompra = models.ForeignKey(OrdenCompra, null=False, blank=False, verbose_name="Orden de Compra")
    articulo = models.ForeignKey(Articulo, null=False, blank=False, verbose_name="Articulo")
    cantidad_pedida = models.DecimalField(verbose_name='Cantidad Pedida', decimal_places=2, blank=True, null=True,
                                       default=0, max_digits=20)
    cantidad_entregada = models.DecimalField(verbose_name='Cantidad Entregada', decimal_places=2, blank=True, null=True,
                                       default=0, max_digits=20)
    costo_compra = models.DecimalField(verbose_name='Costo de Compra', decimal_places=2, blank=True, null=True,
                                       default=0, max_digits=20)
    iva = models.DecimalField(verbose_name='IVA', decimal_places=2, blank=True, null=True,
                                       default=0, max_digits=20)
    unidad_medida_compra = models.CharField(verbose_name='Unidad de Medida de Compra', blank=True, null=True,
                                       default='', max_length=20)
    descripcion =  models.CharField(verbose_name='Descripción de Compra', blank=True, null=True,
                                       default='', max_length=250)

    class Meta:
        verbose_name = "Detalle de Orden de Compra"
        verbose_name_plural = "Detalle de Orden de Compra"

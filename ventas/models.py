# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.forms.models import model_to_dict
from smart_selects.db_fields import ChainedForeignKey
from Logs.controller import Logs
from concurrency.fields import IntegerVersionField
from django.utils.timezone import now
from django.core.validators import RegexValidator

from catalogos.models import Color, Cliente,Corte,Forro,Ojillo, Agujeta, Suela,Linea, Estilo
from users.models import User

# Create your models here.

@python_2_unicode_compatible
class Lote(models.Model):
    numero = models.IntegerField(verbose_name="Número de Lote", null=False, blank=False, default=0)
    estilo = models.ForeignKey(Estilo, null=False, blank=False, verbose_name="Estilo")
    color = models.ForeignKey(Color, null=False, blank=False, verbose_name="Color")
    corte = models.ForeignKey(Corte, null=False, blank=False, verbose_name="Corte")
    forro = models.ForeignKey(Forro, null=False, blank=False, verbose_name="Forro")
    ojillo = models.ForeignKey(Ojillo, null=False, blank=False, verbose_name="Ojillo")
    agujeta = models.ForeignKey(Agujeta, null=False, blank=False, verbose_name="Agujeta")
    suela = models.ForeignKey(Suela, null=False, blank=False, verbose_name="Suela")
    cliente = models.ForeignKey(Cliente, null=False, blank=False, verbose_name="Cliente")
    linea = models.ForeignKey(Linea, null=False, blank=False, verbose_name="Linea")

    observaciones = models.CharField(verbose_name="Observaciones", max_length=600, null=False, blank=True, )
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega", null=False, blank=False,)
    fecha_genera = models.DateField(verbose_name="Fecha de creacion", null=False, blank=False, )
    programa = models.IntegerField(verbose_name="Programa", null=False, blank=False, default=0)
    usuario_genera = models.ForeignKey(User, verbose_name="Usuario que Genera", blank=True, null=False, related_name='%(class)s_requests_created')

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['estilo'] = self.estilo.nombre
        dict['color'] = self.color.nombre
        dict['corte'] = self.corte.nombre
        dict['forro'] = self.forro.nombre
        dict['ojillo'] = self.ojillo.nombre
        dict['agujeta'] = self.agujeta.nombre
        dict['suela'] = self.suela.nombre
        dict['usuario_genera'] = self.usuario_genera.username
        dict['id'] = str(self.id)
        return dict

    def __str__(self):
        return self.folio + ": " + self.folio

    def __unicode__(self):
        return self.folio + ": " + self.folio

@python_2_unicode_compatible
class Pedido(models.Model):
    folio = models.IntegerField(verbose_name="Folio", null=False, blank=False, default=0)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, verbose_name="Cliente")
    fecha_creacion = models.DateField(verbose_name="Fecha de creacion", null=False, blank=False, )
    observaciones = models.TextField(verbose_name="Observaciones", max_length=600, null=False, blank=True)
    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['folio'] = self.folio
        return ans

    def __str__(self):
        return str(self.folio)

    def __unicode__(self):
        return str(self.folio)


@python_2_unicode_compatible
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, null=False, blank=False, verbose_name="Pedido")
    estilo = models.ForeignKey(Estilo, null=False, blank=False, verbose_name="Estilo")
    color = models.ForeignKey(Color, null=False, blank=False, verbose_name="Color")
    corte = models.ForeignKey(Corte, null=False, blank=False, verbose_name="Corte")
    forro = models.ForeignKey(Forro, null=False, blank=False, verbose_name="Forro")
    ojillo = models.ForeignKey(Ojillo, null=False, blank=False, verbose_name="Ojillo")
    agujeta = models.ForeignKey(Agujeta, null=False, blank=False, verbose_name="Agujeta")
    suela = models.ForeignKey(Suela, null=False, blank=False, verbose_name="Suela")
    linea = models.ForeignKey(Linea, null=False, blank=False, verbose_name="Linea")

    descripcion = models.TextField(verbose_name="Descripcion", max_length=600, null=True, blank=True)
    fecha_genera = models.DateField(verbose_name="Fecha de creacion", null=False, blank=False,auto_now=True )

    class Meta:
        verbose_name = "Detalle de Pedido"
        verbose_name_plural = "Detalles de Pedido"

    def to_serializable_dict(self):
        dict = model_to_dict(self)
        dict['pedido'] = self.pedido.folio
        dict['estilo'] = self.estilo.nombre
        dict['color'] = self.color.nombre
        dict['corte'] = self.corte.nombre
        dict['forro'] = self.forro.nombre
        dict['ojillo'] = self.ojillo.nombre
        dict['agujeta'] = self.agujeta.nombre
        dict['suela'] = self.suela.nombre
        dict['id'] = str(self.id)
        return dict

    def __str__(self):
        return str(self.pedido.folio) + ": " + self.pedido.cliente.nombre

    def __unicode__(self):
        return str(self.pedido.folio) + ": " + self.pedido.cliente.nombre


@python_2_unicode_compatible
class ParesPorPunto(models.Model):
    lote = models.ForeignKey(Lote, null=False, blank=False)
    talla = models.IntegerField(verbose_name='Talla',null=False, blank=False, validators=[
        RegexValidator(regex='^[0-9]*$', message='Este campo solo acepta numeros')])
    total_pares = models.IntegerField(verbose_name='Total de Pares',null=False, blank=False,validators=[
        RegexValidator(regex='^[0-9]*$', message='Este campo solo acepta numeros')])

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['talla'] = self.talla
        return ans

    def __str__(self):
        return str(self.talla)

    def __unicode__(self):
        return str(self.talla)

@python_2_unicode_compatible
class ParesPorPuntoPedido(models.Model):
    detalle_pedido = models.ForeignKey(DetallePedido, null=False, blank=False)
    talla = models.IntegerField(verbose_name='Talla',null=False, blank=False, validators=[
        RegexValidator(regex='^[0-9]*$', message='Este campo solo acepta numeros')])
    total_pares = models.IntegerField(verbose_name='Total de Pares',null=False, blank=False,validators=[
        RegexValidator(regex='^[0-9]*$', message='Este campo solo acepta numeros')])

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['talla'] = self.talla
        return ans

    def __str__(self):
        return str(self.talla)

    def __unicode__(self):
        return str(self.talla)
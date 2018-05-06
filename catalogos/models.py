# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.forms.models import model_to_dict
from smart_selects.db_fields import ChainedForeignKey
from Logs.controller import Logs
from concurrency.fields import IntegerVersionField
from django.utils.timezone import now
from django.core.validators import RegexValidator
# Create your models here.

@python_2_unicode_compatible
class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['pais'] = self.nombre
        return ans

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Países'
        verbose_name = "País"

@python_2_unicode_compatible
class Estado(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    pais = models.ForeignKey(Pais, null=False, blank=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nombre

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans

@python_2_unicode_compatible
class Municipio(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    estado = models.ForeignKey(Estado, null=False, blank=False)

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['estado'] = self.estado.nombre
        return ans

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

@python_2_unicode_compatible
class Proveedor(models.Model):
    version = IntegerVersionField()
    nombre = models.CharField(verbose_name='Nombre', max_length=50, null=False, blank=False, editable=True)
    calle = models.CharField(verbose_name='Calle', max_length=50, null=False, blank=False, editable=True)
    numero = models.CharField(verbose_name='Número', max_length=10, null=False, blank=False, editable=True)
    colonia = models.CharField(verbose_name='Colonia', max_length=50, null=False, blank=False, editable=True)
    cp = models.CharField(verbose_name='C.P.', max_length=20, null=False, blank=False, editable=True)
    rfc = models.CharField(verbose_name='RFC', max_length=20, null=False, blank=False, editable=True)
    telefono = models.CharField(verbose_name='Teléfono', max_length=30, null=True, blank=True, editable=True)
    telefono_dos = models.CharField(verbose_name='Teléfono No.2', max_length=30, null=True, blank=True, editable=True)
    email = models.CharField(verbose_name='Correo Electrónico', max_length=60, null=False, blank=False, editable=True)

    # Chained key attributes. Might be duplicated, but it is required to reach the expected behaviour.
    pais = models.ForeignKey(Pais, verbose_name="País", null=False, blank=False)
    estado = ChainedForeignKey(Estado,
                               chained_field="pais",
                               chained_model_field="pais",
                               show_all=False,
                               auto_choose=True,
                               sort=True)
    municipio = ChainedForeignKey(Municipio,
                                  chained_field="estado",
                                  chained_model_field="estado",
                                  show_all=False,
                                  auto_choose=True,
                                  sort=True)

    last_edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Proveedor'

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['nombre'] = str(self.nombre)
        ans['calle'] = str(self.calle)
        ans['numero'] = str(self.numero)
        ans['colonia'] = str(self.colonia)
        ans['municipio'] = str(self.municipio.nombre)
        ans['estado'] = str(self.estado.nombre)
        ans['pais'] = str(self.pais.nombre)
        ans['cp'] = str(self.cp)
        ans['rfc'] = str(self.rfc)

        return ans

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        can_save = True

        if can_save:
            self.last_edit_date = now()
            Logs.log("Guardando un nuevo Proveedor", "Alta")
            super(Proveedor, self).save(*args, **kwargs)
        else:
            Logs.log("No se pudo guardar el proveedor", 'Alta')

@python_2_unicode_compatible
class Cliente(models.Model):
    version = IntegerVersionField()
    nombre = models.CharField(verbose_name='Nombre', max_length=50, null=False, blank=False, editable=True,validators=[
           RegexValidator(
                   regex = '^[a-zA-Z ]*$',
                   message = 'Este campo no debe contener numeros'
               ),
       ])
    calle = models.CharField(verbose_name='Calle', max_length=50, null=False, blank=False, editable=True,validators=[
           RegexValidator(
                   regex = '^[a-zA-Z ]*$',
                   message = 'Este campo no debe contener numeros'
               ),
       ])
    numero = models.CharField(verbose_name='Número', max_length=10, null=False, blank=False, editable=True)
    colonia = models.CharField(verbose_name='Colonia', max_length=50, null=False, blank=False,
                               editable=True,validators=[
           RegexValidator(
                   regex = '^[a-zA-Z ]*$',
                   message = 'Este campo no debe contener numeros'
               ),
       ])
    cp = models.CharField(verbose_name='C.P.', max_length=20, null=False, blank=False, editable=True)
    rfc = models.CharField(verbose_name='RFC', max_length=20, null=False, blank=False, editable=True)
    telefono = models.CharField(verbose_name='Teléfono', max_length=30, null=True, blank=True,
                                editable=True)
    telefono_dos = models.CharField(verbose_name='Teléfono No.2', max_length=30, null=True, blank=True,
                                    editable=True)
    email = models.CharField(verbose_name='Correo Electrónico', max_length=60, null=False, blank=False,
                             editable=True)

    # Chained key attributes. Might be duplicated, but it is required to reach the expected behaviour.
    pais = models.ForeignKey(Pais, verbose_name="País", null=False, blank=False)
    estado = ChainedForeignKey(Estado,
                               chained_field="pais",
                               chained_model_field="pais",
                               show_all=False,
                               auto_choose=True,
                               sort=True)
    municipio = ChainedForeignKey(Municipio,
                                  chained_field="estado",
                                  chained_model_field="estado",
                                  show_all=False,
                                  auto_choose=True,
                                  sort=True)

    last_edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cliente'

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['nombre'] = str(self.nombre)
        ans['calle'] = str(self.calle)
        ans['numero'] = str(self.numero)
        ans['colonia'] = str(self.colonia)
        ans['municipio'] = str(self.municipio.nombre)
        ans['estado'] = str(self.estado.nombre)
        ans['pais'] = str(self.pais.nombre)
        ans['cp'] = str(self.cp)
        ans['rfc'] = str(self.rfc)

        return ans

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        can_save = True

        if can_save:
            self.last_edit_date = now()
            Logs.log("Guardando un nuevo Cliente", "Alta")
            super(Cliente, self).save(*args, **kwargs)
        else:
            Logs.log("No se pudo guardar el cliente", 'Alta')

class DireccionEntrega(models.Model):
    version = IntegerVersionField()
    cliente = models.ForeignKey(Cliente, verbose_name="País", null=False, blank=False)
    calle = models.CharField(verbose_name='Calle', max_length=50, null=False, blank=False, editable=True)
    numero = models.CharField(verbose_name='Número', max_length=10, null=False, blank=False, editable=True)
    colonia = models.CharField(verbose_name='Colonia', max_length=50, null=False, blank=False,
                               editable=True)
    cp = models.CharField(verbose_name='C.P.', max_length=20, null=False, blank=False, editable=True)
    telefono = models.CharField(verbose_name='Teléfono', max_length=30, null=True, blank=True,
                                editable=True)
    latitud = models.FloatField(default=0, blank=True, null=True, )
    longitud = models.FloatField(default=0, blank=True, null=True, )

    # Chained key attributes. Might be duplicated, but it is required to reach the expected behaviour.
    pais = models.ForeignKey(Pais, verbose_name="País", null=False, blank=False)
    estado = ChainedForeignKey(Estado,
                               chained_field="pais",
                               chained_model_field="pais",
                               show_all=False,
                               auto_choose=True,
                               sort=True)
    municipio = ChainedForeignKey(Municipio,
                                  chained_field="estado",
                                  chained_model_field="estado",
                                  show_all=False,
                                  auto_choose=True,
                                  sort=True)

    last_edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Dirección de entrega'

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        ans['nombre'] = str(self.cliente.nombre)
        ans['calle'] = str(self.calle)
        ans['numero'] = str(self.numero)
        ans['colonia'] = str(self.colonia)
        ans['municipio'] = str(self.municipio.nombre)
        ans['estado'] = str(self.estado.nombre)
        ans['pais'] = str(self.pais.nombre)
        ans['cp'] = str(self.cp)

        return ans

    def __str__(self):
        return self.cliente.nombre

    def save(self, *args, **kwargs):
        can_save = True

        if can_save:
            self.last_edit_date = now()
            Logs.log("Guardando un nueva dirección de entrega del cliente " + self.cliente.nombre, "Alta")
            super(DireccionEntrega, self).save(*args, **kwargs)
        else:
            Logs.log("No se pudo guardar la dirección e entrega del cliente " + self.cliente.nombre, 'Alta')

# class UnidadMedida(models.Model):
#     nombre = models.CharField(verbose_name='Nombre', max_length=50, null=False, blank=False, editable=True)
#     numero_unidades = models.CommaSeparatedIntegerField(verbose_name='Número de Unidades', default=0, null=False, blank=False, editable=True)
#     descripcion = models.CharField(verbose_name='Descripción', max_length=50, null=False, blank=False, editable=True)
#
#     class Meta:
#         verbose_name_plural = 'Unidad de Medida'
#
#     def __str__(self):
#         return self.nombre
#
#     def save(self, *args, **kwargs):
#         can_save = True
#
#         if can_save:
#             self.last_edit_date = now()
#             Logs.log("Guardando un nueva Unidad de Medida", "Alta")
#             super(Proveedor, self).save(*args, **kwargs)
#         else:
#             Logs.log("No se pudo guardar la Unidad de Medida", 'Alta')


@python_2_unicode_compatible
class Corte(models.Model):
    nombre = models.CharField(verbose_name="Corte", max_length=200, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='Este campo no debe contener numeros'
            )
        ])
    descripcion = models.TextField(verbose_name="Descripción", max_length=600, null=False, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nombre

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans


@python_2_unicode_compatible
class Forro(models.Model):
    nombre = models.CharField(verbose_name="Forro", max_length=200, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='Este campo no debe contener numeros'
            )
        ])
    descripcion = models.TextField(verbose_name="Descripción", max_length=600, null=False, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nombre

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans


@python_2_unicode_compatible
class Ojillo(models.Model):
    nombre = models.CharField(verbose_name="Ojillo", max_length=200, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='Este campo no debe contener numeros'
            )
        ])
    descripcion = models.TextField(verbose_name="Descripción", max_length=600, null=False, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nombre

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans


@python_2_unicode_compatible
class Agujeta(models.Model):
    nombre = models.CharField(verbose_name="Agujeta", max_length=200, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='Este campo no debe contener numeros'
            )
        ])
    descripcion = models.TextField(verbose_name="Descripción", max_length=600, null=False, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nombre

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans


@python_2_unicode_compatible
class Suela(models.Model):
    nombre = models.CharField(verbose_name="Suela", max_length=200, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='Este campo no debe contener numeros'
            )
        ])
    descripcion = models.TextField(verbose_name="Descripción", max_length=600, null=False, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nombre

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans


@python_2_unicode_compatible
class Linea(models.Model):
    linea_de = models.CharField(verbose_name="De", max_length=5, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[0-9]*$',
                message='Este campo debe contener numeros'
            )
        ])
    linea_a = models.CharField(verbose_name="A", max_length=5, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[0-9]*$',
                message='Este campo debe contener numeros'
            )
        ])
    descripcion = models.TextField(verbose_name="Descripción", max_length=600, null=False, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.de + "-" + self.a

    def __unicode__(self):  # __unicode__ on Python 2
        return self.de + "-" + self.a

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans


@python_2_unicode_compatible
class Estilo(models.Model):
    nombre = models.CharField(verbose_name="Estilo", max_length=200, null=False, blank=True, validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='Este campo no debe contener numeros'
            )
        ])
    imagen = models.FileField(verbose_name="Foto", upload_to="media/estilos/")
    descripcion = models.TextField(verbose_name="Descripción", max_length=600, null=False, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

    def __unicode__(self):  # __unicode__ on Python 2
        return self.nombre

    def to_serializable_dict(self):
        ans = model_to_dict(self)
        ans['id'] = str(self.id)
        return ans

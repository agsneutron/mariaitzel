# coding=utf-8
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.contrib import messages
from django.forms import SelectDateWidget
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
from tinymce.widgets import TinyMCE

from users.models import ERPUser
from django.utils.translation import ugettext as _

import datetime

from ventas.models import ParesPorPuntoPedido, DetallePedido, Pedido
from django.utils.safestring import mark_safe
from Logs.controller import Logs
import os
from django.conf import settings
from django.contrib.admin import widgets

from django.contrib.admin.widgets import RelatedFieldWidgetWrapper


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ('estilo', 'color', 'corte', 'forro', 'ojillo', 'agujeta', 'suela', 'linea',)


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('folio', 'cliente', 'fecha_creacion', 'observaciones')

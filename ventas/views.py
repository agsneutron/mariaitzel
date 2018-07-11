# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from models import Pedido


import operator
import urllib
import locale
import decimal
from datetime import date

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.forms.models import modelformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext, loader
import datetime
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView


from django.db.models import Q
import json

from django.shortcuts import render, redirect

# Create your views here.

class PedidoDetailView(generic.DetailView):
    model = Pedido
    template_name = "ventas/pedido-detalle.html"

class PedidoListView(ListView):
    model = Pedido
    template_name = "ventas/pedido-list.html"
    query = None
    title_list = "Pedidos"

    """
       Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(PedidoListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            PedidoListView.query = query
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(folio__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(observaciones__icontains=q) for q in query_list))
            )
        else:
            PedidoListView.query = ''

        return result

    def get_context_data(self, **kwargs):
        context = super(PedidoListView, self).get_context_data(**kwargs)
        context['title_list'] = PedidoListView.title_list
        context['query'] = PedidoListView.query
        context['query_string'] = '&q=' + PedidoListView.query
        context['has_query'] = (PedidoListView.query is not None) and (PedidoListView.query != "")
        return context
    def dispatch(self, request, *args, **kwargs):
        return super(PedidoListView, self).dispatch(request, args, kwargs)

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from rest_framework import generics

from .models import Presupuesto
from GestionDePagos.mixins import SearchMixin, UpdateInactivoMixin

# Create your views here.
class PresupuestoListView(SearchMixin, ListView):
    model = Presupuesto
    context_object_name = 'presupuestos'
    template_name = 'presupuestos/presupuesto_list.html'
    search_fields = ['cliente__nombre', 'cliente__apellido', 'id']
    paginate_by = 10

class PresupuestoDetailView(DetailView):
    model = Presupuesto
    context_object_name = 'presupuesto'
    template_name = 'presupuestos/presupuesto_detail.html'

class PresupuestoCreateView(CreateView):
    model = Presupuesto
    template_name = 'clientes/cliente_form.html'
    fields = ['fecha', 'validez', 'cliente', 'observaciones']

class PresupuestoUpdateView(UpdateInactivoMixin, UpdateView):
    model = Presupuesto
    template_name = 'clientes/cliente_form.html'

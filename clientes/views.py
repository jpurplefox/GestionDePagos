from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from rest_framework import generics

from .models import Cliente
from .forms import ClienteForm
from .serializers import ClienteSerializer
from GestionDePagos.mixins import SearchMixin, UpdateInactivoMixin

# Create your views here.
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'

    def form_valid(self, form):
        result = super(ClienteCreateView, self).form_valid(form)
        messages.success(self.request, "El cliente {nombre} fue creado con éxito".format(nombre=self.object))
        return result

class ClienteUpdateView(UpdateInactivoMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'

    def form_valid(self, form):
        result = super(ClienteUpdateView, self).form_valid(form)
        messages.success(self.request, "El cliente {nombre} fue actualizado con éxito".format(nombre=self.object))
        return result

class ClienteListView(SearchMixin, ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'clientes/cliente_list.html'
    search_fields = ['nombre', 'apellido', 'email', 'telefono']
    paginate_by = 10

class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'clientes/cliente_detail.html'

class ClienteAPIList(generics.ListCreateAPIView):
    model = Cliente
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteAPIDetail(generics.RetrieveAPIView):
    model = Cliente
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


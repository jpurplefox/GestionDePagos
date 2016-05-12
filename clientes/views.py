from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers

from .models import Cliente, Vehiculo
from .forms import ClienteForm, VehiculoForm
from Talleres.mixins import SearchMixin, UpdateInactivoMixin

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
    search_fields = ['nombre', 'apellido', 'email', 'dni', 'vehiculos__patente']
    paginate_by = 10

class ClienteDetailView(SearchMixin, ListView):
    model = Vehiculo
    context_object_name = 'vehiculos'
    template_name = 'clientes/cliente_detail.html'
    search_fields = ['modelo__nombre', 'patente']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ClienteDetailView, self).get_queryset()
        cliente_pk = self.kwargs['pk']
        queryset = queryset.filter(cliente__pk=cliente_pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        cliente_pk = self.kwargs['pk']
        cliente = get_object_or_404(Cliente, pk=cliente_pk)
        context['cliente'] = cliente
        return context

def clientes_json(request):
    clientes = serializers.serialize('json', Cliente.objects.all(), indent=2)
    return HttpResponse(clientes, content_type='application/json')
    #clientes = Cliente.objects.all()
    #return JsonResponse(clientes, encoder=serializers)

#Vehiculos
class VehiculoDetailView(DetailView):
    model = Vehiculo
    context_object_name = 'vehiculo'
    template_name = 'clientes/vehiculo_detail.html'

class VehiculoUpdateView(UpdateInactivoMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'clientes/vehiculo_form.html'

    def form_valid(self, form):
        result = super(VehiculoUpdateView, self).form_valid(form)
        messages.success(self.request, "El vehiculo {vehiculo} fue actualizado con éxito".format(vehiculo=self.object))
        return result

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'clientes/vehiculo_form.html'

    def dispatch(self, request, *args, **kwargs):
        cliente_pk = self.kwargs['cliente_id']
        self.cliente = get_object_or_404(Cliente, pk=cliente_pk)
        if not self.cliente.activo:
            messages.error(self.request, "El cliente {cliente} no está activo por lo que no se le pueden agregar vehiculos".format(cliente=self.cliente))
            return HttpResponseRedirect(self.cliente.get_absolute_url())
        return super(VehiculoCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VehiculoCreateView, self).get_context_data(**kwargs)
        context['cliente'] = self.cliente
        return context

    def form_valid(self, form):
        cliente_pk = self.kwargs['cliente_id']
        cliente = get_object_or_404(Cliente, pk=cliente_pk)
        form.instance.cliente = cliente

        result = super(VehiculoCreateView, self).form_valid(form)
        messages.success(self.request, "El vehiculo {nombre} fue creado con éxito".format(nombre=self.object))
        return result
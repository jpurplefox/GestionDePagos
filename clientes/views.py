from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import Cliente
from .forms import ClienteForm

# Create your views here.
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'

    def form_valid(self, form):
        result = super(ClienteCreateView, self).form_valid(form)
        messages.success(self.request, "El cliente {nombre} fue creado con éxito".format(nombre=self.object))
        return result

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/cliente_form.html'

    def form_valid(self, form):
        result = super(ClienteUpdateView, self).form_valid(form)
        messages.success(self.request, "El cliente {nombre} fue actualizado con éxito".format(nombre=self.object))
        return result

class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'clientes/cliente_detail.html'

class ClienteListView(ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'clientes/cliente_list.html'
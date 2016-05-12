from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers

from .models import Cliente
from .forms import ClienteForm
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
    search_fields = ['nombre', 'apellido', 'email', 'telefono']
    paginate_by = 10

class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'clientes/cliente_detail.html'

def clientes_json(request):
    clientes = serializers.serialize('json', Cliente.objects.all(), indent=2)
    return HttpResponse(clientes, content_type='application/json')
    #clientes = Cliente.objects.all()
    #return JsonResponse(clientes, encoder=serializers)

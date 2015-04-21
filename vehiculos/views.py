from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .models import Marca, Modelo
from .forms import MarcaForm, ModeloForm
from Talleres.mixins import SearchMixin

# Create your views here.
#Marca
class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'vehiculos/marca_form.html'

    def form_valid(self, form):
        result = super(MarcaCreateView, self).form_valid(form)
        messages.success(self.request, "La marca {nombre} fue creada con éxito".format(nombre=self.object))
        return result

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'vehiculos/marca_form.html'

    def form_valid(self, form):
        result = super(MarcaUpdateView, self).form_valid(form)
        messages.success(self.request, "La marca {nombre} fue actualizada con éxito".format(nombre=self.object))
        return result

class MarcaDetailView(SearchMixin, ListView):
    model = Modelo
    context_object_name = 'modelos'
    template_name = 'vehiculos/marca_detail.html'
    search_fields = ['nombre',]

    def get_queryset(self):
        queryset = super(MarcaDetailView, self).get_queryset()
        marca_pk = self.kwargs['pk']
        queryset = queryset.filter(marca__pk=marca_pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(MarcaDetailView, self).get_context_data(**kwargs)
        marca_pk = self.kwargs['pk']
        marca = get_object_or_404(Marca, pk=marca_pk)
        context['marca'] = marca
        return context

class MarcaListView(SearchMixin, ListView):
    model = Marca
    context_object_name = 'marcas'
    template_name = 'vehiculos/marca_list.html'
    search_fields = ['nombre',]

#Modelo
class ModeloCreateView(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'vehiculos/modelo_form.html'

    def get_context_data(self, **kwargs):
        context = super(ModeloCreateView, self).get_context_data(**kwargs)
        marca_pk = self.kwargs['marca_id']
        marca = get_object_or_404(Marca, pk=marca_pk)
        context['marca'] = marca
        return context

    def form_valid(self, form):
        marca_id = self.kwargs['marca_id']
        marca = Marca.objects.get(id=marca_id)
        form.instance.marca = marca

        result = super(ModeloCreateView, self).form_valid(form)
        messages.success(self.request, "El modelo {nombre} fue creado con éxito".format(nombre=self.object))
        return result

class ModeloUpdateView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'vehiculos/modelo_form.html'

    def form_valid(self, form):
        result = super(ModeloUpdateView, self).form_valid(form)
        messages.success(self.request, "El modelo {nombre} fue actualizado con éxito".format(nombre=self.object))
        return result

class ModeloDetailView(DetailView):
    model = Modelo
    context_object_name = 'modelo'
    template_name = 'vehiculos/modelo_detail.html'
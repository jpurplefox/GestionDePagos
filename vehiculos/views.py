from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import Marca
from .forms import MarcaForm
from Talleres.mixins import SearchMixin

# Create your views here.
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

class MarcaDetailView(DetailView):
    model = Marca
    context_object_name = 'marca'
    template_name = 'vehiculos/marca_detail.html'

class MarcaListView(SearchMixin, ListView):
    model = Marca
    context_object_name = 'marcas'
    template_name = 'vehiculos/marca_list.html'
    search_fields = ['nombre',]
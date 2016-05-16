from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse
from rest_framework import generics

from .models import Servicio
from .forms import ServicioForm
from .serializers import ServicioSerializer
from GestionDePagos.mixins import SearchMixin, UpdateInactivoMixin

# Create your views here.
class ServicioCreateView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/servicio_form.html'

    def form_valid(self, form):
        result = super(ServicioCreateView, self).form_valid(form)
        messages.success(self.request, "El servicio {servicio} fue creado con éxito".format(servicio=self.object))
        return result

class ServicioUpdateView(UpdateInactivoMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/servicio_form.html'

    def form_valid(self, form):
        result = super(ServicioUpdateView, self).form_valid(form)
        messages.success(self.request, "El servicio {servicio} fue actualizado con éxito".format(servicio=self.object))
        return result

class ServicioListView(SearchMixin, ListView):
    model = Servicio
    context_object_name = 'servicios'
    template_name = 'servicios/servicio_list.html'
    search_fields = ['descripcion']
    paginate_by = 10

class ServicioDetailView(DetailView):
    model = Servicio
    context_object_name = 'servicio'
    template_name = 'servicios/servicio_detail.html'

class ServicioAPIList(generics.ListCreateAPIView):
    model = Servicio
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioAPIDetail(generics.RetrieveAPIView):
    model = Servicio
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


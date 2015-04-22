from django.conf.urls import url
from . import views

urlpatterns = [
	#Clientes
    url(r'^clientes/$', views.ClienteListView.as_view(), name='cliente_list'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetailView.as_view(), name='cliente_detail'),
    url(r'^cliente/(?P<pk>[0-9]+)/edit/$', views.ClienteUpdateView.as_view(), name='cliente_update'),
    url(r'^cliente/new/$', views.ClienteCreateView.as_view(), name='cliente_create'),

    #Vehiculos
    url(r'^vehiculo/(?P<pk>[0-9]+)/$', views.VehiculoDetailView.as_view(), name='vehiculo_detail'),
    url(r'^vehiculo/(?P<pk>[0-9]+)/edit/$', views.VehiculoUpdateView.as_view(), name='vehiculo_update'),
    url(r'^vehiculo/(?P<cliente_id>[0-9]+)/new/$', views.VehiculoCreateView.as_view(), name='vehiculo_create'),
]
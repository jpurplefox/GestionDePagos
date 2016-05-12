from django.conf.urls import url
from . import views

urlpatterns = [
	#Clientes
    url(r'^clientes/$', views.ClienteListView.as_view(), name='cliente_list'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetailView.as_view(), name='cliente_detail'),
    url(r'^cliente/(?P<pk>[0-9]+)/edit/$', views.ClienteUpdateView.as_view(), name='cliente_update'),
    url(r'^cliente/new/$', views.ClienteCreateView.as_view(), name='cliente_create'),

    url(r'^json/clientes/$', views.clientes_json, name='cliente_list_json'),
]

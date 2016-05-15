from django.conf.urls import url
from . import views

urlpatterns = [
	#Clientes
    url(r'^$', views.ClienteListView.as_view(), name='cliente_list'),
    url(r'^/(?P<pk>[0-9]+)$', views.ClienteDetailView.as_view(), name='cliente_detail'),
    url(r'^/(?P<pk>[0-9]+)/edit$', views.ClienteUpdateView.as_view(), name='cliente_update'),
    url(r'^/new$', views.ClienteCreateView.as_view(), name='cliente_create'),
]

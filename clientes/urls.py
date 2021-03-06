from django.conf.urls import url
from . import views

urlpatterns = [
	#Clientes
    url(r'^$', views.ClienteListView.as_view(), name='cliente_list'),
    url(r'^(?P<pk>[0-9]+)$', views.ClienteDetailView.as_view(), name='cliente_detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.ClienteUpdateView.as_view(), name='cliente_update'),
    url(r'^new$', views.ClienteCreateView.as_view(), name='cliente_create'),
    url(r'^API$', views.ClienteAPIList.as_view(), name='API_cliente_list'),
    url(r'^API/(?P<pk>[0-9]+)$', views.ClienteAPIDetail.as_view(), name='API_cliente_detail'),
]

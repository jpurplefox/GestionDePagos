from django.conf.urls import url
from . import views

urlpatterns = [
	#Marcas
    url(r'^marcas/$', views.MarcaListView.as_view(), name='marca_list'),
    url(r'^marca/(?P<pk>[0-9]+)/$', views.MarcaDetailView.as_view(), name='marca_detail'),
    url(r'^marca/(?P<pk>[0-9]+)/edit/$', views.MarcaUpdateView.as_view(), name='marca_update'),
    url(r'^marca/new/$', views.MarcaCreateView.as_view(), name='marca_create'),
    #Modelos
    url(r'^modelo/(?P<pk>[0-9]+)/$', views.ModeloDetailView.as_view(), name='modelo_detail'),
    url(r'^modelo/(?P<pk>[0-9]+)/edit/$', views.ModeloUpdateView.as_view(), name='modelo_update'),
    url(r'^modelo/(?P<marca_id>[0-9]+)/new/$', views.ModeloCreateView.as_view(), name='modelo_create'),
]
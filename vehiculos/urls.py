from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^marcas/$', views.MarcaListView.as_view(), name='marca_list'),
    url(r'^marca/(?P<pk>[0-9]+)/$', views.MarcaDetailView.as_view(), name='marca_detail'),
    url(r'^marca/(?P<pk>[0-9]+)/edit/$', views.MarcaUpdateView.as_view(), name='marca_update'),
    url(r'^marca/new/$', views.MarcaCreateView.as_view(), name='marca_create'),
]
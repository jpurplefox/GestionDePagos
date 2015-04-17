from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ClienteListView.as_view(), name='cliente_list'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetailView.as_view(), name='cliente_detail'),
    url(r'^new/$', views.ClienteCreateView.as_view(), name='cliente_create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ClienteUpdateView.as_view(), name='cliente_update'),
]
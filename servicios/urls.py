from django.conf.urls import url
from . import views

urlpatterns = [
	#Servicios
    url(r'^servicios/$', views.ServicioListView.as_view(), name='servicio_list'),
    url(r'^servicio/(?P<pk>[0-9]+)/$', views.ServicioDetailView.as_view(), name='servicio_detail'),
    url(r'^servicio/(?P<pk>[0-9]+)/edit/$', views.ServicioUpdateView.as_view(), name='servicio_update'),
    url(r'^servicio/new/$', views.ServicioCreateView.as_view(), name='servicio_create'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
	#Presupuestos
    url(r'^$', views.PresupuestoListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)$', views.PresupuestoDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.PresupuestoUpdateView.as_view(), name='update'),
    url(r'^new$', views.PresupuestoCreateView.as_view(), name='create'),
    #url(r'^API$', views.ClienteAPIList.as_view(), name='API_list'),
    #url(r'^API/(?P<pk>[0-9]+)$', views.ClienteAPIDetail.as_view(), name='API_detail'),
]

from django.conf.urls import include, url
from django.contrib import admin
from .views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes', include('clientes.urls', namespace='clientes')),
    url(r'^servicios', include('servicios.urls', namespace='servicios')),
]

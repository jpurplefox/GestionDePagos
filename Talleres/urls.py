from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes/', include('clientes.urls', namespace='clientes')),
)

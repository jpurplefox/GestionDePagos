from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Talleres.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes/', include('clientes.urls', namespace='clientes')),
)

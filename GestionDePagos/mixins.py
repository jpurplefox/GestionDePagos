from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages

class SearchMixin():
    search_fields = []
    search_attribute = 'search'

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        search = self.request.GET.get(self.search_attribute)

        if search:
            query_filter = Q()
            for field in self.search_fields:
                query_filter = query_filter | Q(**{field+'__contains': search})

            queryset = queryset.filter(query_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SearchMixin, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context

class UpdateInactivoMixin():
    def dispatch(self, request, *args, **kwargs):
        objeto = self.get_object()
        if not objeto.activo:
            messages.error(self.request, "El objeto {objeto} no está activo por lo que no puede editarse".format(objeto=objeto))
            return HttpResponseRedirect(objeto.get_absolute_url())
        return super(UpdateInactivoMixin, self).dispatch(request, *args, **kwargs)
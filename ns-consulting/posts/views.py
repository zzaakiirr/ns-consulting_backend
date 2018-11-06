import operator
from functools import reduce

from django.db.models import Q
from django.views.generic import ListView
from django.urls.exceptions import NoReverseMatch

from .models import PostPluginModel

from .search_helpers import get_duplicate_ids


class PostSearchListView(ListView):
    model = PostPluginModel
    template_name = 'posts/search_results.html'

    def get_queryset(self):
        search_results = super(PostSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if not query:
            return None

        query_list = query.split()
        search_results = search_results.filter(
            reduce(
                operator.and_,
                (Q(body__icontains=q) for q in query_list)
            ) | reduce(
                operator.and_,
                (Q(body__icontains=q.capitalize()) for q in query_list)
            ) | reduce(
                operator.and_,
                (Q(body__icontains=q.upper()) for q in query_list)
            ) | reduce(
                operator.and_,
                (Q(body__icontains=q.lower()) for q in query_list)
            )
        ).exclude(id__in=get_duplicate_ids())

        return search_results

    def get_context_data(self, **kwargs):
        context = super(PostSearchListView, self).get_context_data(**kwargs)

        query = self.request.GET.get('q')
        if not query:
            context['search_query'] = ''
        else:
            context['search_query'] = query

        search_results = self.get_queryset()
        context['search_results'] = search_results

        return context

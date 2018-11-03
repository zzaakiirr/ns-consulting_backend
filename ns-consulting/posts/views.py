import operator
from functools import reduce

from django.db.models import Q
from django.views.generic import ListView

from .models import PostPluginModel


class PostSearchListView(ListView):
    model = PostPluginModel
    template_name = 'posts/search_results.html'

    def get_queryset(self):
        search_result = super(PostSearchListView, self).get_queryset()
        query = self.request.GET.get('q')

        if query:
            query_list = query.split()
            search_result = search_result.filter(
                reduce(
                    operator.and_,
                    (Q(body__icontains=q) for q in query_list)
                )
            )

        return search_result

    def get_context_data(self, **kwargs):
        context = super(PostSearchListView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')

        context['search_query'] = query
        context['posts'] = self.get_queryset()

        return context

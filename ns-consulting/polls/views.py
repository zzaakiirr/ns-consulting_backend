from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Choice, Poll

from .vote_helpers import update_percents


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def vote(request, poll_id, choice_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    selected_choice = poll.choice_set.get(pk=choice_id)

    selected_choice.votes += 1
    selected_choice.save()

    update_percents(poll)
    request.session['poll_has_been_voted'] = True
    return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))

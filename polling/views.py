from django.shortcuts import render
from django.views.generic import ListView, DetailView

from polling.models import Poll


class PollListView(ListView):
    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):
    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        poll = self.get_object()
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
        context = {"poll": poll}
        return render(request, "polling/detail.html", context)

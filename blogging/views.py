from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post
from django.template import loader


# Create your views here.


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class BlogListView(ListView):
    template_name = "blogging/list.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )

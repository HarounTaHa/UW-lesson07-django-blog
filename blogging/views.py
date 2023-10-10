from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets, permissions
from blogging.serializers import PostSerializers, UserSerializer
from blogging.models import Post


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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited posts.
    """

    queryset = Post.objects.all().order_by("-published_date")
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticated]

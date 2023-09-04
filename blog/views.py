from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    permission_denied_message = "You have to be logged in to create a post!"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        Post.objects.create(**form.cleaned_data, author=self.request.user)
        return HttpResponseRedirect("/")


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

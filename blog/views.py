from typing import Any, Optional
from django.db import models
from django.db.models import QuerySet
from django.db.models.query import QuerySet
from django.urls import reverse
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    paginate_by = 10
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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def get_success_url(self) -> str:
        return reverse("post-detail", args=[self.kwargs["pk"]])

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        Post.objects.update(**form.cleaned_data, author=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = "/"

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False

    def get_success_url(self) -> str:
        messages.success(self.request, f"Your post has been successfully deleted.")
        return "/"


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

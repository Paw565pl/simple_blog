from typing import Any
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import Post

# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.select_related("author").all()
    template_name = "blog/home.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-last_update"]


class UserPostListView(ListView):
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(get_user_model(), username=self.kwargs.get("username"))
        return (
            Post.objects.filter(author=user)
            .select_related("author")
            .order_by("-last_update")
        )


class PostDetailView(DetailView):
    queryset = Post.objects.select_related("author").all()
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    permission_denied_message = "You have to be logged in to create a post!"
    success_url = reverse_lazy("blog_home")
    success_message = "Your post has been successfully created."

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    queryset = Post.objects.select_related("author").all()
    fields = ["title", "content"]
    success_message = "Your post has been successfully updated."

    def get_success_url(self) -> str:
        return reverse_lazy("post_detail", args=[self.kwargs["pk"]])

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False


class PostDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    queryset = Post.objects.select_related("author").all()
    context_object_name = "post"
    success_url = reverse_lazy("blog_home")
    success_message = "Your post has been successfully deleted."

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:  # type: ignore
            return True
        return False


def about(request):  # TODO: use template view
    return render(request, "blog/about.html", {"title": "About"})

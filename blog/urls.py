from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.PostListView.as_view(), name="blog-home"),
    path("post/new/", v.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", v.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/edit/", v.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", v.PostDeleteView.as_view(), name="post-delete"),
    path("about/", v.about, name="blog-about"),
]

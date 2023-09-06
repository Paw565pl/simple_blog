from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.PostListView.as_view(), name="blog_home"),
    path(
        "posts/user/<str:username>", v.UserPostListView.as_view(), name="user_profile"
    ),
    path("post/new/", v.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", v.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", v.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", v.PostDeleteView.as_view(), name="post_delete"),
    path("about/", v.about, name="blog_about"),
]

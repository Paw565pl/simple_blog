from django.urls import path
from . import views as v

urlpatterns = [
    # path("", v.home, name="blog-home"),
    path("", v.PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", v.PostDetailView.as_view(), name="post-detail"),
    path("about/", v.about, name="blog-about"),
]

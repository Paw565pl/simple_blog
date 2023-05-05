from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home, name="blog-home"),
    path("about/", v.about, name="blog-about"),
]

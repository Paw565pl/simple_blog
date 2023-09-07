from django.contrib.auth import get_user_model
from model_bakery import baker
from blog.models import Post
import pytest


@pytest.fixture
def posts():
    def get_posts(author, quantity=10):
        return baker.make(Post, author=author, _quantity=quantity)

    return get_posts


@pytest.fixture
def create_posts(client):
    def do_create_post(post: Post):
        return client.post("/post/new/", post)

    return do_create_post


@pytest.fixture
def user():
    return baker.make(get_user_model())


@pytest.fixture
def authenticate_user(client, user):
    return client.force_login(user)

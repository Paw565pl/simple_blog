from django.contrib.auth import get_user_model
from model_bakery import baker
from blog.models import Post
from django.test import Client
import pytest


@pytest.fixture
def posts():
    def get_posts(author, quantity=10):
        return baker.make(Post, author=author, _quantity=quantity)

    return get_posts


@pytest.fixture
def user():
    return baker.make(get_user_model())


@pytest.fixture
def authenticate_user(client, user):
    return client.force_login(user)

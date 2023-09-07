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
def get_post(client):
    def do_get_post(id):
        return client.get(f"/post/{id}/")

    return do_get_post


@pytest.fixture
def get_posts_by_user(client):
    def do_get_posts_by_user(username):
        return client.get(f"/posts/user/{username}")

    return do_get_posts_by_user


@pytest.fixture
def create_post(client):
    def do_create_post(post: Post):
        return client.post("/post/new/", post)

    return do_create_post


@pytest.fixture
def full_update_post(client):
    def do_full_update_post(id: int, updated_post: Post):
        return client.put(f"/post/{id}/edit/", updated_post)

    return do_full_update_post


@pytest.fixture
def delete_post(client):
    def do_delete_post(id):
        return client.delete(f"/post/{id}/delete/")

    return do_delete_post


@pytest.fixture
def user():
    return baker.make(get_user_model())


@pytest.fixture
def users():
    def get_users(quantity=2):
        return [baker.make(get_user_model()) for _ in range(quantity)]

    return get_users


@pytest.fixture
def authenticated_user(client, user):
    client.force_login(user)
    return user

from model_bakery import baker
from blog.models import Post
import pytest


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
def update_post(client):
    def do_update_post(id: int, updated_post: Post):
        return client.post(f"/post/{id}/edit/", updated_post)

    return do_update_post


@pytest.fixture
def delete_post(client):
    def do_delete_post(id):
        return client.delete(f"/post/{id}/delete/")

    return do_delete_post


@pytest.fixture
def bake_posts():
    def do_bake_posts(author, quantity=10):
        return baker.make(Post, author=author, _quantity=quantity)

    return do_bake_posts

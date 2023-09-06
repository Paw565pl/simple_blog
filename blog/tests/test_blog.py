import pytest
from random import randint
from django.contrib.auth import get_user_model
from model_bakery import baker
from blog.models import Post


@pytest.mark.django_db
class TestRetrievePost:
    def test_if_post_exists_returns_200(self, client):
        posts_quantity = 10
        user = baker.make(get_user_model())
        posts = baker.make(Post, author=user, _quantity=posts_quantity)

        for post in posts:
            response = client.get(f"/post/{post.id}/")  # type: ignore

            assert response.status_code == 200

    def test_if_post_does_not_exist_returns_404(self, client):
        post_id = randint(1, 10)

        response = client.get(f"/post/{post_id}/")

        assert response.status_code == 404

    def test_if_user_posts_exist_returns_200(self, client):
        posts_quantity = 10
        user = baker.make(get_user_model())
        baker.make(Post, author=user, _quantity=posts_quantity)

        response = client.get(f"/posts/user/{user.username}")  # type: ignore

        assert response.status_code == 200

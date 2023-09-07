from random import randint
from blog.models import Post
import pytest


@pytest.mark.django_db
class TestRetrievePost:
    def test_if_post_exists_returns_200(self, client, user, posts):
        posts = posts(user)

        for post in posts:
            response = client.get(f"/post/{post.id}/")

            assert response.status_code == 200

    def test_if_post_does_not_exist_returns_404(self, client):
        post_id = randint(1, 10)

        response = client.get(f"/post/{post_id}/")

        assert response.status_code == 404

    def test_if_user_posts_exist_returns_200(self, client, user, posts):
        posts = posts(user)

        response = client.get(f"/posts/user/{user.username}")

        assert response.status_code == 200


@pytest.mark.django_db
class TestCreatePost:
    def test_if_user_is_anonymous_returns_302(self, create_posts):
        data = {"title": "test", "content": "test"}
        response = create_posts(data)

        assert response.status_code == 302
        assert response.url == "/login/?next=/post/new/"

    def test_if_data_is_invalid_does_not_create(
        self,
        authenticate_user,
        create_posts,
    ):
        data = {"title": "", "content": ""}
        response = create_posts(data)

        assert Post.objects.count() == 0

    def test_if_data_is_valid_creates_post(self, authenticate_user, create_posts):
        data = {"title": "test", "content": "test"}
        response = create_posts(data)

        created_post = Post.objects.get(title="test", content="test")

        assert Post.objects.count() == 1
        assert (
            Post.objects.first().__dict__.items()
            >= {"title": "test", "content": "test"}.items()
        )

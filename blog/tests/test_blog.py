from random import randint
from blog.models import Post
import pytest


@pytest.mark.django_db
class TestRetrievePost:
    def test_if_post_exists_returns_200(self, user, posts, get_post):
        posts = posts(user)

        for post in posts:
            response = get_post(post.id)

            assert response.status_code == 200

    def test_if_post_does_not_exist_returns_404(self, get_post):
        post_id = randint(1, 10)

        response = get_post(post_id)

        assert response.status_code == 404

    def test_if_user_posts_exist_returns_200(self, user, posts, get_posts_by_user):
        posts = posts(user)

        response = get_posts_by_user(user.username)

        assert response.status_code == 200


@pytest.mark.django_db
class TestCreatePost:
    valid_data = {"title": "test", "content": "test"}
    invalid_data = {"title": "", "content": ""}

    def test_if_user_is_anonymous_returns_302(self, create_post):
        response = create_post(self.valid_data)

        assert response.status_code == 302
        assert response.url == "/login/?next=/post/new/"

    def test_if_data_is_invalid_does_not_create(
        self,
        authenticated_user,
        create_post,
    ):
        create_post(self.invalid_data)

        assert Post.objects.count() == 0

    def test_if_data_is_valid_creates_post(self, authenticated_user, create_post):
        create_post(self.valid_data)

        assert Post.objects.count() == 1
        assert Post.objects.first().__dict__.items() >= self.valid_data.items()


@pytest.mark.django_db
class TestUpdatePost:
    def test_if_user_is_not_author_returns_403(
        self, client, users, posts, full_update_post
    ):
        (user1, user2) = users()
        (post,) = posts(user1, 1)
        client.force_login(user2)

        id = post.id
        updated_data = {"title": "test1", "content": "test1"}
        response = full_update_post(id, updated_data)

        assert response.status_code == 403


@pytest.mark.django_db
class TestDeletePost:
    def test_if_user_is_not_author_returns_403(self, client, users, posts, delete_post):
        (user1, user2) = users()
        (post,) = posts(user1, 1)
        client.force_login(user2)

        id = post.id
        response = delete_post(id)

        assert Post.objects.count() == 1
        assert response.status_code == 403

    def test_if_data_is_valid_returns_302(self, authenticated_user, posts, delete_post):
        (post,) = posts(authenticated_user, 1)

        id = post.id
        response = delete_post(id)

        assert Post.objects.count() == 0
        assert response.status_code == 302
        assert response.url == "/"

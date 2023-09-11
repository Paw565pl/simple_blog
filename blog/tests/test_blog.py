from random import randint
from django.forms.models import model_to_dict
from blog.models import Post
import pytest


@pytest.mark.django_db
class TestRetrievePost:
    def test_if_post_exists_returns_200(self, bake_user, bake_posts, get_post):
        bake_posts = bake_posts(bake_user)

        for post in bake_posts:
            response = get_post(post.id)

            assert response.status_code == 200

    def test_if_post_does_not_exist_returns_404(self, get_post):
        post_id = randint(1, 10)

        response = get_post(post_id)

        assert response.status_code == 404

    def test_if_user_posts_exist_returns_200(
        self, bake_user, bake_posts, get_posts_by_user
    ):
        bake_posts = bake_posts(bake_user)

        response = get_posts_by_user(bake_user.username)

        assert response.status_code == 200


@pytest.mark.django_db
class TestCreatePost:
    valid_data = {"title": "test", "content": "test"}
    invalid_data = {"title": "", "content": ""}

    def test_if_user_is_anonymous_returns_login_view(self, create_post):
        response = create_post(self.valid_data)

        assert response.status_code == 302
        assert response.url == "/login/?next=/post/new/"
        assert Post.objects.count() == 0

    def test_if_data_is_invalid_does_not_create(
        self,
        authenticated_user,
        create_post,
    ):
        response = create_post(self.invalid_data)

        assert response.status_code == 200
        assert Post.objects.count() == 0

    def test_if_data_is_valid_creates(self, authenticated_user, create_post):
        response = create_post(self.valid_data)

        assert response.status_code == 302
        assert response.url == "/"
        assert Post.objects.count() == 1

        created_post = Post.objects.first()

        if created_post:
            created_post_dict = model_to_dict(
                created_post, fields=list(self.valid_data.keys())
            )
            assert created_post_dict == self.valid_data


@pytest.mark.django_db
class TestUpdatePost:
    def test_if_user_is_not_author_returns_403(
        self, client, bake_users, bake_posts, update_post
    ):
        (user1, user2) = bake_users()
        (post,) = bake_posts(user1, 1)
        client.force_login(user2)

        id = post.id
        updated_data = {"title": "test1", "content": "test1"}
        response = update_post(id, updated_data)

        assert response.status_code == 403

        post_dict = model_to_dict(
            Post.objects.get(id=id), fields=list(updated_data.keys())
        )
        assert post_dict != updated_data

    def test_if_data_is_valid_updates(
        self, authenticated_user, bake_posts, update_post
    ):
        (post,) = bake_posts(authenticated_user, 1)

        id = post.id
        updated_data = {"title": "test1", "content": "test1"}
        response = update_post(id, updated_data)

        assert response.status_code == 302
        assert response.url == "/post/23/"

        updated_post_dict = model_to_dict(
            Post.objects.get(id=id), fields=list(updated_data.keys())
        )
        assert updated_post_dict == updated_data


@pytest.mark.django_db
class TestDeletePost:
    def test_if_user_is_not_author_returns_403(
        self, client, bake_users, bake_posts, delete_post
    ):
        (user1, user2) = bake_users()
        (post,) = bake_posts(user1, 1)
        client.force_login(user2)

        id = post.id
        response = delete_post(id)

        assert response.status_code == 403
        assert Post.objects.count() == 1

    def test_if_data_is_valid_deletes(
        self, authenticated_user, bake_posts, delete_post
    ):
        (post,) = bake_posts(authenticated_user, 1)

        id = post.id
        response = delete_post(id)

        assert response.status_code == 302
        assert response.url == "/"
        assert Post.objects.count() == 0

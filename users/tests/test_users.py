from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
import pytest


valid_data = {
    "username": "user1",
    "email": "user1@email.com",
    "password1": "mysecretpassword123",
    "password2": "mysecretpassword123",
}
invalid_data = {
    "username": "user2",
    "email": "",
    "password1": "mysecretpassword123",
    "password2": "mysecretpassword456",
}


@pytest.mark.django_db
class TestRegister:
    def test_if_data_is_invalid_does_not_register(self, register_user):
        response = register_user(invalid_data)

        assert response.context["form_show_errors"]
        assert get_user_model().objects.count() == 0

    def test_if_user_already_exists_does_not_register(self, register_user):
        register_user(valid_data)
        response = register_user(valid_data)

        assert response.context["form_show_errors"]
        assert get_user_model().objects.count() == 1

    def test_if_data_is_valid_registeres(self, register_user):
        response = register_user(valid_data)

        assert response.status_code == 302
        assert response.url == "/login/"
        assert get_user_model().objects.count() == 1


@pytest.mark.django_db
class TestLogin:
    def test_if_user_does_not_exist_does_not_login(self, login_user):
        response = login_user(valid_data["username"], valid_data["password1"])

        assert response.context["form_show_errors"]
        assert response.context["user"].is_anonymous

    # TODO: test if user tries to login twice

    def test_if_data_is_valid_logins(self, register_user, login_user):
        register_user(valid_data)
        response = login_user(valid_data["username"], valid_data["password1"])

        assert response.status_code == 302
        assert response.wsgi_request.user.is_authenticated
        assert response.wsgi_request.user.username == valid_data["username"]

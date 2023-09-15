from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
import pytest


valid_data = {
    "username": "user1",
    "email": "user1@email.com",
    "password1": "mysecretpassword123",
    "password2": "mysecretpassword123",
}
invalid_data = {
    "username": "user2*",
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

    def test_if_data_is_valid_logins(self, register_user, login_user):
        register_user(valid_data)
        response = login_user(valid_data["username"], valid_data["password1"])

        assert response.status_code == 302
        assert response.wsgi_request.user.is_authenticated
        assert response.wsgi_request.user.username == valid_data["username"]


@pytest.mark.django_db
class TestProfile:
    def test_if_user_is_anonymous_returns_login_view(self, update_user):
        response = update_user(
            {"username": valid_data["username"], "email": valid_data["password1"]}
        )

        assert response.status_code == 302
        assert response.url == "/login/?next=/profile/"

    def test_if_data_is_invalid_does_not_update(
        self, register_user, login_user, update_user
    ):
        register_user(valid_data)
        login_user(valid_data["username"], valid_data["password1"])

        response = update_user({"username": invalid_data["username"]})

        assert response.context["form_show_errors"]

        user = get_user_model().objects.first()
        if user:
            assert user.get_username() == valid_data["username"]

    def test_if_data_is_valid_updates(self, register_user, login_user, update_user):
        register_user(valid_data)
        login_user(valid_data["username"], valid_data["password1"])

        updated_user_data = {
            "username": valid_data["username"] + "TEST",
            "email": valid_data["email"],
        }
        update_user(updated_user_data)

        user = get_user_model().objects.first()
        if user:
            assert (
                model_to_dict(user, fields=list(updated_user_data.keys()))
                == updated_user_data
            )

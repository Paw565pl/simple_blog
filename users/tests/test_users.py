from django.contrib.auth import get_user_model
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

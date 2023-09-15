import pytest


@pytest.fixture
def register_user(client):
    def do_register_user(user_data):
        user_data["h-captcha-response"] = "10000000-aaaa-bbbb-cccc-000000000001"
        return client.post("/register/", user_data)

    return do_register_user


@pytest.fixture
def login_user(client):
    def do_login_user(username, password):
        return client.post(
            "/login/",
            {
                "username": username,
                "password": password,
                "h-captcha-response": "10000000-aaaa-bbbb-cccc-000000000001",
            },
        )

    return do_login_user


@pytest.fixture
def update_user(client):
    def do_update_user(user_data):
        return client.post("/profile/", user_data)

    return do_update_user

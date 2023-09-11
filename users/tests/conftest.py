import pytest


@pytest.fixture
def register_user(client):
    def do_register_user(user_data):
        return client.post("/register/", user_data)

    return do_register_user

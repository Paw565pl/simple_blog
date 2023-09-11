from django.contrib.auth import get_user_model
from model_bakery import baker
import pytest


@pytest.fixture
def bake_user():
    return baker.make(get_user_model())


@pytest.fixture
def bake_users():
    def do_bake_users(quantity=2):
        return [baker.make(get_user_model()) for _ in range(quantity)]

    return do_bake_users


@pytest.fixture
def authenticated_user(client, bake_user):
    client.force_login(bake_user)
    return bake_user

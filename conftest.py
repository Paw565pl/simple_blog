from django.contrib.auth import get_user_model
from model_bakery import baker
import pytest


@pytest.fixture
def bake_user():
    def do_bake_user(**kwargs):
        return baker.make(get_user_model(), **kwargs)

    return do_bake_user


@pytest.fixture
def bake_users():
    def do_bake_users(quantity=2):
        return [baker.make(get_user_model()) for _ in range(quantity)]

    return do_bake_users


@pytest.fixture
def authenticated_user(client, bake_user):
    baked_user = bake_user()
    client.force_login(baked_user)
    return baked_user

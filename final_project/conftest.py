import pytest
from django.contrib.auth import get_user_model


@pytest.fixture()
def user1(db):
    profile = get_user_model()
    return profile.objects.create_user(email='test-user@test.com', user_name='test-user', password='password')
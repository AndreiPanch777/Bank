import pytest
import random

from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = CreateUserRequest(
        username=f"Maxc{random.randint(1000, 9999)}",
        password="Pas!sw0rd",
        role="ROLE_USER"
    )
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def credit_user_request(api_manager):
    user_request = CreateUserRequest(
        username=f"Credit{random.randint(1000, 9999)}",
        password="Pas!sw0rd",
        role="ROLE_CREDIT_SECRET"
    )
    api_manager.admin_steps.create_user(user_request)
    return user_request
from typing import Generator

import pytest
from databases import Database
from fastapi.testclient import TestClient

from app.core.config import settings
from app.fastapi_app import app
from tests.utils.user import authentication_token_from_email
from tests.utils.utils import get_superuser_token_headers


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_dependency_overrides() -> Generator:
    yield
    app.dependency_overrides = {}


@pytest.fixture
def superuser_token_headers(api_client: TestClient) -> dict[str, str]:
    return get_superuser_token_headers(api_client)


@pytest.fixture
def normal_user_token_headers(api_client: TestClient, db: Database) -> dict[str, str]:
    return authentication_token_from_email(
        api_client=api_client, email=settings.EMAIL_TEST_USER, db=db
    )

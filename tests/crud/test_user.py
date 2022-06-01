import pytest
from databases import Database

from app import crud
from app.core.security import verify_password
from app.schemas.user import UserIn, UserUpdate
from tests.utils.utils import random_email, random_lower_string

pytestmark = pytest.mark.asyncio


async def test_create_user(pg_db: Database) -> None:
    email = random_email()
    password = random_lower_string()
    first_name = random_lower_string()
    last_name = random_lower_string()
    user_in = UserIn(email=email, password=password, first_name=first_name, last_name=last_name)
    user = await crud.user.create(pg_db, obj_in=user_in)

    assert user.email == email
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert hasattr(user, "hashed_password")
    assert verify_password(password, user.hashed_password)


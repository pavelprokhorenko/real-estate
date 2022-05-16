from pydantic import EmailStr

from app.schemas import BaseSchema


class BaseUser(BaseSchema):
    email: EmailStr


class UserIn(BaseUser):
    hashed_password: str
    first_name: str
    last_name: str
    phone_number: str
    is_active: bool
    is_superuser: bool


class UserOut(BaseUser):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    is_active: bool
    is_superuser: bool

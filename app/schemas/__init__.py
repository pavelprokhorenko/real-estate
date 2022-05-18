# flake8: noqa
from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True


from .message import *
from .token import *
from .user import *

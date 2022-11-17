from pydantic import validator
from pydantic.types import constr
from src.core import Constants
from src.schema.payloads.base import BasePayload


class RegisterUserSchema(BasePayload):
    username: constr(min_length=4)
    login: constr(min_length=4)
    password: constr(min_length=8, max_length=20)
    password_confirm: str

    @validator("password_confirm")
    def validate_password_confirm(cls, value, values):
        if value != values["password"]:
            raise ValueError("password do not match")
        return value

    @validator("login")
    def login_validator(cls, value):
        if not all(later in Constants.LOGIN_WHITE_LIST_SYMBOLS for later in value):
            raise ValueError("not allowed symbols")
        return value

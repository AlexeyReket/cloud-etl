from src.schema.payloads.base import BasePayload


class LoginSchema(BasePayload):
    login: str
    password: str

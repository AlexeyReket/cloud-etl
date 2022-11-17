from src.schema.responses.base import BaseResponse


class LoginUserResponseSchema(BaseResponse):
    id: int
    token: str
    username: str

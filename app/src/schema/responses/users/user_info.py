from src.schema.responses.base import BaseResponse


class UserInfoResponseSchema(BaseResponse):
    id: int
    login: str
    username: str
    is_super_user: bool

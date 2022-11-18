import functools

from fastapi import Header, HTTPException
from src.api.contexvars import user_info
from src.schema.responses.users.user_info import UserInfoResponseSchema
from src.services import auth
from src.services.database import UserService


async def authorization(
    token_: str = Header(..., alias="x-authorization", regex=r"Bearer .+", description="Bearer your-token-here")
) -> UserInfoResponseSchema:
    decoded_data = auth.decode_token(token_.split(" ")[1])
    if not decoded_data.get("id"):
        raise HTTPException(status_code=401, detail="wrong token")
    user_info_ = await UserService.get_user_info(decoded_data["id"])
    user_info.set(user_info_)
    return user_info_


def check_superuser(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        user = user_info.get()
        if not user.is_super_user:
            raise HTTPException(status_code=403, detail="forbidden")
        result = await func(*args, **kwargs)
        return result

    return wrapper

import http

from fastapi import HTTPException
from src.database.models import UserModel
from src.database.repositories.users import UserRepository
from src.schema.responses.users import UserInfoResponseSchema
from src.services import auth


class UserService:
    @classmethod
    async def check_login_and_username_for_free(cls, login: str, username: str) -> None:
        users_logins = await UserRepository.find_all_logins()
        if login in users_logins:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST, detail="not unique login"
            )
        users_names = await UserRepository.find_all_usernames()
        if username in users_names:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST, detail="not unique username"
            )

    @classmethod
    async def create(cls, login: str, password: str, username: str) -> UserModel:
        user = await UserRepository.save(
            UserModel(
                login=login,
                hashed_password=auth.get_password_hash(password),
                username=username,
            )
        )
        return user

    @classmethod
    async def get_user_info(cls, user_id: int) -> UserInfoResponseSchema:
        user = await UserRepository.find_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=http.HTTPStatus.UNAUTHORIZED, detail="unknown user"
            )
        return UserInfoResponseSchema.from_orm(user)

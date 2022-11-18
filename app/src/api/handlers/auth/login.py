import http
from datetime import datetime

from fastapi import HTTPException
from src.database.repositories import UserRepository
from src.schema.payloads.users import LoginSchema
from src.schema.responses.users import LoginUserResponseSchema
from src.services import auth


class LoginHandler:
    @classmethod
    async def handle(cls, payload: LoginSchema) -> LoginUserResponseSchema:
        user = await UserRepository.find_by_login(payload.login)
        if not user:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST, detail="wrong login"
            )
        if not auth.verify_password(payload.password, user.hashed_password):
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST, detail="wrong password"
            )
        return LoginUserResponseSchema(
            token=auth.encode_data(
                {"id": user.id, "created_at": datetime.utcnow().isoformat()}
            ),
            username=user.username,
            id=user.id,
        )

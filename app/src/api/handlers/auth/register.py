from src.database.models import UserModel
from src.database.repositories import UserRepository
from src.schema.payloads.users import RegisterUserSchema
from src.schema.responses.users import UserInfoResponseSchema
from src.services import auth
from src.services.database import UserService


class RegisterHandler:
    @classmethod
    async def handle(cls, payload: RegisterUserSchema) -> UserInfoResponseSchema:
        await UserService.check_login_and_username_for_free(
            payload.login, payload.username
        )
        return await UserRepository.save(
            UserModel(
                username=payload.username,
                login=payload.login,
                hashed_password=auth.get_password_hash(payload.password),
            )
        )

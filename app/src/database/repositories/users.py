from typing import List, Optional

from sqlalchemy import select
from src.database.models import UserModel
from src.database.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    model = UserModel

    @classmethod
    async def find_all_usernames(cls) -> List[str]:
        query = select(UserModel.username)
        result = await cls.execute(query)
        return cls.all(result)

    @classmethod
    async def find_all_logins(cls) -> List[str]:
        query = select(UserModel.login)
        result = await cls.execute(query)
        return cls.all(result)

    @classmethod
    async def find_by_id(cls, user_id: int) -> Optional[UserModel]:
        query = select(UserModel).filter_by(id=user_id)
        result = await cls.execute(query)
        return cls.first(result)

    @classmethod
    async def find_by_login(cls, login: str) -> Optional[UserModel]:
        query = select(UserModel).filter_by(login=login)
        result = await cls.execute(query)
        return cls.first(result)

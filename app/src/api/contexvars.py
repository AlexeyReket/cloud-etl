from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession
from src.schema.responses.users import UserInfoResponseSchema

user_info: ContextVar[UserInfoResponseSchema] = ContextVar("user_info")

db_session: ContextVar[AsyncSession] = ContextVar("db-session")

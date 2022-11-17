import functools

from fastapi import Request
from src.api.contexvars import db_session
from src.database.core import async_session_factory


async def create_session(request: Request, call_next):
    async with async_session_factory() as session_:
        db_session.set(session_)
        response = await call_next(request)
        return response


def commit_after(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        await db_session.get().commit()
        return result

    return wrapper

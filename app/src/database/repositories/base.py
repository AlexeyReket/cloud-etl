from src.api.contexvars import db_session


class BaseRepository:
    @staticmethod
    async def execute(query, flush: bool = False):
        result = await db_session.get().execute(query)
        if flush:
            await db_session.get().flush()
        return result

    @staticmethod
    async def flush() -> None:
        await db_session.get().flush()

    @classmethod
    async def save(cls, entity):
        db_session.get().add(entity)
        await cls.flush()
        return entity

    @staticmethod
    def all(result):
        return result.scalars().all()

    @staticmethod
    def first(result):
        return result.scalars().first()

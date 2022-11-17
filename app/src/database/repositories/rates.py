from sqlalchemy import select
from src.database.models import ExchangeRatesModel

from .base import BaseRepository


class RatesRepository(BaseRepository):
    model = ExchangeRatesModel

    @classmethod
    async def get_by_date(cls, date, *, is_actual: bool = None) -> list[model]:
        query = select(ExchangeRatesModel).filter(ExchangeRatesModel.date == date)
        if is_actual is not None:
            query = query.filter(ExchangeRatesModel.is_actual == is_actual)
        result = await cls.execute(query)
        return cls.all(result)

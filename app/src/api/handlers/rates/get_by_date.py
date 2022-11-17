import datetime

from src.database.repositories import RatesRepository


class GetByDateHandler:
    @classmethod
    async def handle(cls, date: datetime.date):
        rates = await RatesRepository.get_by_date(date, is_actual=True)
        return rates

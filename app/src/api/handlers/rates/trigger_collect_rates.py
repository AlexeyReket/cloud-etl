import datetime

import requests
from fastapi import HTTPException
from src.core import settings
from src.schema.responses.rates import CollectRatesResponse


class TriggerCollectRates:
    @classmethod
    async def handle(cls, date: datetime.date) -> CollectRatesResponse:
        response = requests.get(
            settings.FUNCTION_URL,
            json={"date": date.isoformat(), "api_key": settings.API_KEY},
        )
        if response.ok:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)

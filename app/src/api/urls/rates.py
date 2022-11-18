import datetime

from fastapi import APIRouter, Depends, status
from src.api.handlers.rates import GetByDateHandler, TriggerCollectRates
from src.api.middlewares import authorization, check_superuser
from src.schema.responses import ShortRateResponse
from src.schema.responses.rates import CollectRatesResponse

router = APIRouter(
    prefix="/rates", dependencies=[Depends(authorization)], tags=["rates"]
)


@router.get("", response_model=list[ShortRateResponse])
async def get_rate_for_date(date: datetime.date):
    return await GetByDateHandler.handle(date)


@router.post(
    "/collect",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=CollectRatesResponse,
)
@check_superuser
async def trigger_collect_rates(date: datetime.date):
    return await TriggerCollectRates.handle(date)

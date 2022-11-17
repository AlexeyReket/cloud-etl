from .base import BaseResponse


class ShortRateResponse(BaseResponse):
    id: int
    rate_code: str
    value: float
    nominal: int

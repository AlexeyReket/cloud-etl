import dataclasses
import datetime


@dataclasses.dataclass
class EventData:
    date: datetime.date
    api_key: str


@dataclasses.dataclass
class RatesSchema:
    rate_code: str
    value: float
    nominal: int


@dataclasses.dataclass
class RepositoryRatesSchema(RatesSchema):
    id: int
    date: datetime.date

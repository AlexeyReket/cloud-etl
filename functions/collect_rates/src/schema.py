import dataclasses
import datetime


@dataclasses.dataclass
class EventData:
    date: datetime.date
    api_key: str


@dataclasses.dataclass
class VoluteSchema:
    rate_code: str
    value: float
    nominal: int


@dataclasses.dataclass
class RepositoryVoluteSchema(VoluteSchema):
    id: int
    date: datetime.date

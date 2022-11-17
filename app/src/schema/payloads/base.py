from pydantic.main import BaseModel
from src.services.utils import to_camel_case


class BasePayload(BaseModel):
    class Config:
        alias_generator = to_camel_case

from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "stg"
    API_KEY: str
    YANDEXCLOUD_TOKEN: str
    DATABASE_URI: str
    DATABASE_SCHEMA: str
    FUNCTION_URL: str
    SECRET_KEY: str
    ALLOWED_ORIGINS: List[str] = ["*"]
    ALLOWED_METHODS: List[str] = ["*"]
    ALLOWED_HEADERS: List[str] = ["*"]


settings = Settings("env/.env")

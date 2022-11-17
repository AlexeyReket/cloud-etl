from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from src.core import settings

metadata_obj = MetaData(
    schema=settings.DATABASE_SCHEMA, quote_schema=settings.DATABASE_SCHEMA
)
Base = declarative_base(metadata=metadata_obj)

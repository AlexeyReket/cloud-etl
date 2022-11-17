from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, func
from src.database.models.base import Base


class ExchangeRatesModel(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    rate_code = Column(String(10), nullable=False)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    is_actual = Column(Boolean, nullable=False, default=True)
    nominal = Column(Integer)

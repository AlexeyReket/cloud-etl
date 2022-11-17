from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    login = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_super_user = Column(Boolean, default=False)

import http
from typing import Any

from jose import jwt
from passlib.context import CryptContext
from src.core.settings_ import settings
from fastapi import HTTPException
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def decode_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(http.HTTPStatus.UNAUTHORIZED, detail="wrong token")


def encode_data(data: Any):
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)

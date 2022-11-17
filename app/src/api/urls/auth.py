from fastapi import APIRouter, Depends, status
from src.api.handlers.auth import LoginHandler, RegisterHandler
from src.api.middlewares import authorization, commit_after
from src.schema.payloads.users import LoginSchema, RegisterUserSchema
from src.schema.responses.users import UserInfoResponseSchema

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/check-token")
async def check_token(user_info: UserInfoResponseSchema = Depends(authorization)):
    return user_info


@router.post("/register", status_code=status.HTTP_201_CREATED)
@commit_after
async def register(payload: RegisterUserSchema):
    return await RegisterHandler.handle(payload)


@router.post("/login")
async def login(payload: LoginSchema):
    return await LoginHandler.handle(payload)

from fastapi import APIRouter

from .auth import router as auth_router
from .rates import router as rates_router

router = APIRouter(prefix="/api")
router.include_router(rates_router)
router.include_router(auth_router)

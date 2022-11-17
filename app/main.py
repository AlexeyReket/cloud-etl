from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.middlewares import create_session
from src.api.urls import router
from src.core import settings
from src.exceptions.handlers import include_exception_handlers


def get_app():
    app_ = FastAPI()
    app_.include_router(router)
    include_exception_handlers(app_)
    app_.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )
    app_.middleware("http")(create_session)
    return app_


app = get_app()

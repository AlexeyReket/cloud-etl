from fastapi import FastAPI, HTTPException, Request, responses


def include_exception_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def handle_http_exception(request: Request, exp: HTTPException):
        return responses.JSONResponse(exp.detail, exp.status_code)

    @app.exception_handler(HTTPException)
    async def handle_http_exception(request: Request, exp: HTTPException):
        return responses.JSONResponse(exp.detail, exp.status_code)

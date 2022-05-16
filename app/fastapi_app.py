from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.api.v1.router import api_router

app = FastAPI(
    title="Real Estate API",
    openapi_url="/v1/openapi.json",
)

app.include_router(api_router, prefix="/v1")


@app.middleware("http")
async def catch_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"msg": str(exc)}),
        )

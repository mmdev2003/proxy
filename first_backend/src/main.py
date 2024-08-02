import sys

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

sys.path.append("/usr/src/app/src")
sys.path.append("/usr/src/app")

import api

app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)
api.include_routers(app)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SheetsGPT API",
        version="1.0.0",
        summary="Помогайте фронтендерам",
        description="Хотелось бы верить, что эта API имеет место быть и мы не выстрелилт себе в колено",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.on_event("startup")
async def app_startup():
    from db import models
    from utils.logger import logger

    await models.init_models()
    logger.info("Init database")
    await logger.complete()


@app.get("/api/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

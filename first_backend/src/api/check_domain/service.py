from fastapi.responses import JSONResponse

from utils import config, client as c
from utils.logger import logger
from . import repository


async def check_domain(session, public_domain):
    try:
        domain = await repository.check_domain(session, public_domain)

        logger.info("Check domain DONE")
        await logger.complete()

        return domain

    except Exception as e:
        logger.error("Check domain ERROR", extra=e)
        await logger.complete()
        raise e


async def redirect_request(request_type, request_data):
    res = {}
    client = c.Client(config.get('FIRST_BACKEND'))

    try:
        if request_type == "GET":
            res = await client.redirect_to_get(request_data)

        logger.success("Redirected to first backend /redirect SUCCESS")
        await logger.complete()

        return JSONResponse(res, status_code=200)

    except Exception as e:
        logger.error("Redirect request ERROR", extra=e)
        await logger.complete()
        raise e


async def server_error(e):
    err_msg = {
        "message": "check domain failed"
    }
    return JSONResponse(err_msg, status_code=500)

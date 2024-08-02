from fastapi.responses import JSONResponse

from utils import encryption, config, client as c
from utils.logger import logger

second_backend = config.get("SECOND_BACKEND")
key = config.get("CRYPTO_KEY")


async def redirect_request(encrypted_data, request_type):
    res = {}
    client = c.Client(config.get('SECOND_BACKEND'))

    request_data = await encryption.decode_data(encrypted_data, key)

    try:
        if request_type == "GET":
            res = await client.redirect_to_get(request_data)

        logger.success("Redirect to second backend /redirect SUCCESS")
        await logger.complete()

        return JSONResponse(res, status_code=200)

    except Exception as e:
        logger.error("Redirect to second backend /redirect ERROR", extra=e)
        await logger.complete()
        raise e


async def server_error(e):
    err_msg = {
        "message": "capture failed"
    }
    return JSONResponse(err_msg, status_code=500)

from fastapi.responses import JSONResponse

from utils import encryption, config, client as c
from utils.logger import logger

key = config.get('CRYPTO_KEY')


async def redirect_to_second_backend(request_data):
    client = c.Client(config.get("SECOND_BACKEND"))

    encrypted_data = await encryption.encode_data(request_data, key)

    body = {
        "encrypted_data": encrypted_data,
        "request_type": "GET"
    }
    print(body)
    try:
        # Response from second backend
        res = await client.redirect_to_second_backend(body)
        print(res)

        # Decode response from second backend
        res = await encryption.decode_data(res["encrypted_data"], key)

        logger.success("GET request to second backend SUCCESS")
        await logger.complete()

        return JSONResponse(res, status_code=200)

    except Exception as e:
        logger.error("GET request to second backend ERROR", extra=e)
        await logger.complete()
        raise e


async def server_error(e):
    err_msg = {
        "message": "redirect get failed"
    }
    return JSONResponse(err_msg, status_code=500)

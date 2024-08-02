from fastapi.responses import JSONResponse
from utils import encryption, config, client as c
from utils.logger import logger

key = config.get("CRYPTO_KEY")


async def redirect_to_domain(domain, cookies, headers, body, url_path):
    client = c.Client(domain)
    try:
        res = await client.request_original_domain(url_path, body, headers, cookies)

        res = {
            "encrypted_data": await encryption.encode_data(res, key)
        }

        logger.success("Original request SUCCESS")
        await logger.complete()

        return JSONResponse(res, status_code=200)

    except Exception as e:
        logger.error("Original request ERROR", extra=e)
        await logger.complete()
        raise e


async def server_error(e):
    err_msg = {
        "message": "redirect"
    }
    return JSONResponse(err_msg, status_code=500)

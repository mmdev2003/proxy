import json

import cryptocode
from utils.logger import logger


async def encode_data(request_data, key):
    try:
        request_data_str = json.dumps(request_data)
        encrypted_data = cryptocode.encrypt(request_data_str, key)

        logger.info("Encode data DONE")
        await logger.complete()

        return str(encrypted_data)

    except Exception as e:
        logger.error("Encode data ERROR", extra=e)
        await logger.complete()
        raise e


async def decode_data(encrypted_data, key):
    try:
        body_str = cryptocode.decrypt(encrypted_data, key)
        body = json.loads(body_str)

        logger.info("Decode data DONE")
        await logger.complete()

        return body

    except Exception as e:
        logger.error("Decode data ERROR", extra=e)
        await logger.complete()
        raise e

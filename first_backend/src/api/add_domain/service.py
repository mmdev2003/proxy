from fastapi.responses import JSONResponse


from . import repository
from .schema import ResponseSchema
from utils.logger import logger


async def add_domain(session, domain, public_domain):

    domain_data = {
        "public_domain": public_domain,
        "domain": domain
    }

    await repository.add_domain(session, domain_data)

    logger.success("Domain added")
    await logger.complete()

    res = ResponseSchema(
        public_domain=public_domain
    )

    return JSONResponse(res.dict(), status_code=200)


async def server_error(e):
    logger.error("Add domain failed", extra=e)
    await logger.complete()

    err_msg = {
        "message": "Add domain failed"
    }
    return JSONResponse(err_msg, status_code=500)

from db.connection import get_session
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse

from . import service
from .schema import RequestSchema, ResponseSchema

router = APIRouter()
path = "/check_domain"


@router.post(path, response_model=ResponseSchema)
async def check_domain(
        request_data: RequestSchema,
        session=Depends(get_session)
):
    try:
        request_data = request_data.dict()

        request_type = request_data["request_type"]
        public_domain = request_data["public_domain"]

        domain = await service.check_domain(session, public_domain)

        if domain:
            request_data["domain"] = domain
            res = await service.redirect_request(request_type, request_data)
            return res

        return JSONResponse({"message": "domain does not exist in db"}, 200)

    except Exception as e:
        return await service.server_error(e)

from fastapi import APIRouter

from . import service
from .schema import RequestSchema, ResponseSchema

router = APIRouter()
path = "/capture"


@router.post(path, response_model=ResponseSchema)
async def capture(
    request_data: RequestSchema
):
    try:
        request_data = request_data.dict()

        request_type = request_data["request_type"]
        encrypted_data = request_data["encrypted_data"]

        return await service.redirect_request(encrypted_data, request_type)

    except Exception as e:
        return await service.server_error(e)

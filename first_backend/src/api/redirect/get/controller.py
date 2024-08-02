from fastapi import APIRouter

from . import service
from .schema import RequestSchema, ResponseSchema

router = APIRouter()
path = "/redirect/get"


@router.post(path, response_model=ResponseSchema)
async def get_redirect(
        request_data: RequestSchema,
):
    try:
        request_data = request_data.dict()

        return await service.redirect_to_second_backend(request_data)

    except Exception as e:
        return await service.server_error(e)

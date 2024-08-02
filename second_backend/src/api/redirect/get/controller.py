from fastapi import APIRouter

from . import service
from .schema import RequestSchema, ResponseSchema

router = APIRouter()
path = "/redirect/get"


@router.post(path, response_model=ResponseSchema)
async def request(
        request_data: RequestSchema
):
    try:
        request_data = request_data.dict()
        domain = request_data["domain"]
        cookies = request_data["cookies"]
        headers = request_data["headers"]
        body = request_data["body"]
        url_path = request_data["path"]

        return await service.redirect_to_domain(domain, cookies, headers, body, url_path)

    except Exception as e:
        return await service.server_error(e)

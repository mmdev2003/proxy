from fastapi import Depends, APIRouter

from . import service
from .schema import RequestSchema, ResponseSchema
from db.connection import get_session

router = APIRouter()
path = "/add/domain"


@router.post(path, response_model=ResponseSchema)
async def add_domain_router(
    requests_data: RequestSchema,
    session=Depends(get_session)
):
    try:
        requests_data = requests_data.dict()

        domain = requests_data["domain"]
        public_domain = requests_data["public_domain"]

        return await service.add_domain(session, domain, public_domain)

    except Exception as e:
        return await service.server_error(e)

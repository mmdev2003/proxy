from typing import Dict

from pydantic import BaseModel


class RequestSchema(BaseModel):
    encrypted_data: str
    request_type: str


class ResponseSchema(BaseModel):
    encrypted_data: str

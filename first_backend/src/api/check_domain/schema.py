from typing import Dict

from pydantic import BaseModel


class RequestSchema(BaseModel):
    public_domain: str
    path: str
    request_type: str
    body: Dict
    headers: Dict
    cookies: Dict


class ResponseSchema(BaseModel):
    body: Dict
    headers: Dict
    cookies: Dict
    content: str
    text: str

from pydantic import BaseModel


class RequestSchema(BaseModel):
    public_domain: str
    domain: str


class ResponseSchema(BaseModel):
    public_domain: str

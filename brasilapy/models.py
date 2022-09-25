from pydantic import BaseModel


class BaseReturnModel(BaseModel):
    class Config:
        allow_mutation = False
        orm_mode = False


class Bank(BaseReturnModel):
    ispb: str
    name: str
    code: int | None
    fullName: str

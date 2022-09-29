from datetime import date

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


# Classes for CEP
class CEP(BaseReturnModel):
    cep: str
    state: str
    city: str
    neighborhood: str
    street: str
    service: str


class LatLonPoint(BaseReturnModel):
    longitude: float
    latitude: float


class CEPLocation(BaseReturnModel):
    type: str
    coordinates: LatLonPoint


class CEPv2(CEP):
    location: CEPLocation


class DDD(BaseReturnModel):
    state: str
    cities: list[str]


class FeriadoNacional(BaseReturnModel):
    date: date
    name: str
    type: str

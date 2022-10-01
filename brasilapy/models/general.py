from datetime import date, datetime

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


class FipeVeiculo(BaseReturnModel):
    nome: str
    valor: int


class FipePreco(BaseReturnModel):
    valor: str
    marca: str
    modelo: str
    anoModelo: int
    combustivel: str
    codigoFipe: str
    mesReferencia: str
    tipoVeiculo: int
    siglaCombustivel: str
    dataConsulta: str


class FipeTabelaItem(BaseReturnModel):
    codigo: int
    mes: str


class IbgeMunicipio(BaseReturnModel):
    nome: str
    codigo_ibge: str


class IbgeEstadoRegiao(BaseReturnModel):
    id: int
    sigla: str
    nome: str


class IbgeEstado(BaseReturnModel):
    id: int
    sigla: str
    nome: str
    regiao: IbgeEstadoRegiao


class RegistroBrDominio(BaseReturnModel):
    status_code: int
    status: str
    fqdn: str
    fqdnace: str
    exempt: bool
    hosts: list[str]
    publication_status: str
    expires_at: datetime
    suggestions: list[str]


class TaxaJuros(BaseReturnModel):
    nome: str
    valor: float

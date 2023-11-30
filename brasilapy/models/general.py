from datetime import date, datetime

from pydantic import BaseModel


class BaseReturnModel(BaseModel):
    class Config:
        allow_mutation = False
        orm_mode = False

class Corretora (BaseReturnModel):
    bairro: str
    cep: str
    cnpj: str
    codigo_cvm: str
    complemento: str
    data_inicio_situacao: str
    data_patrimonio_liquido: str
    data_registro: str
    email: str
    logradouro: str
    municipio: str
    nome_social: str
    nome_comercial: str
    pais: str
    status: str
    telefone: str
    type: str
    uf: str
    valor_patrimonio_liquido: str

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
    neighborhood: str | None
    street: str | None
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


class NCM(BaseReturnModel):
    codigo: str
    descricao: str
    data_inicio: date
    data_fim: date | None
    tipo_ato: str
    numero_ato: str
    ano_ato: str

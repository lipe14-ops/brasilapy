from datetime import date

from .general import BaseReturnModel


class CNAE(BaseReturnModel):
    codigo: int
    descricao: str


class SocioAdmin(BaseReturnModel):
    pais: str | None
    nome_socio: str
    codigo_pais: str | None
    faixa_etaria: str
    cnpj_cpf_do_socio: str  # with a filter
    qualificacao_socio: str
    codigo_faixa_etaria: int
    data_entrada_sociedade: date
    identificador_de_socio: int
    cpf_representante_legal: str
    nome_representante_legal: str
    codigo_qualificacao_socio: int
    qualificacao_representante_legal: str
    codigo_qualificacao_representante_legal: int


class CNPJ(BaseReturnModel):
    uf: str
    cep: str
    qsa: list[SocioAdmin]
    cnpj: str
    pais: str | None
    email: str | None
    porte: str
    bairro: str
    numero: str
    ddd_fax: str
    municipio: str
    logradouro: str
    cnae_fiscal: int
    codigo_pais: int | None
    complemento: str
    codigo_porte: int
    razao_social: str
    nome_fantasia: str
    capital_social: int
    ddd_telefone_1: str
    ddd_telefone_2: str
    opcao_pelo_mei: bool
    descricao_porte: str
    codigo_municipio: int
    cnaes_secundarios: list[CNAE]
    natureza_juridica: str
    situacao_especial: str
    opcao_pelo_simples: bool
    situacao_cadastral: int
    data_opcao_pelo_mei: date | None
    data_exclusao_do_mei: date | None
    cnae_fiscal_descricao: str
    codigo_municipio_ibge: int
    data_inicio_atividade: date | None
    data_situacao_especial: str | None
    data_opcao_pelo_simples: date | None
    data_situacao_cadastral: date | None
    nome_cidade_no_exterior: str
    codigo_natureza_juridica: int
    data_exclusao_do_simples: date | None
    motivo_situacao_cadastral: int
    ente_federativo_responsavel: str
    identificador_matriz_filial: int
    qualificacao_do_responsavel: int
    descricao_situacao_cadastral: str
    descricao_tipo_de_logradouro: str
    descricao_motivo_situacao_cadastral: str
    descricao_identificador_matriz_filial: str

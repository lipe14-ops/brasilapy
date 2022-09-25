"""
'get_banks': '/banks/v1/',
'get_bank': '/banks/v1/{code}',
'get_cep_v1': '/cep/v1/{cep}',
'get_cep_v2': '/cep/v2/{cep}',
'get_cnpj': '/cnpj/v1/{cnpj}',
'get_ddd': '/ddd/v1/{ddd}',
'get_feriados_nacionais': '/feriados/v1/{ano}',
'get_fipe_veiculo': '/fipe/marcas/v1/{tipoVeiculo}',
'get_fipe_precos': '/fipe/preco/v1/{codigoFipe}',
'get_fipe_tabelas': '/banks/v1/',
'get_ibge_municipios': '/ibge/municipios/v1/{siglaUF}?providers=dados-abertos-br,gov,wikipedia',
'get_ibge_estados': '/ibge/uf/v1',
'get_ibge_estado': '/ibge/uf/v1/{code}',
'get_registro_br': '/regsitrobr/v1/{domain}',
'get_taxas': '/taxas/v1',
'get_taxa': '/taxas/v1/{sigla}'
"""
from brasilapy.models import Bank
from brasilapy.processor import RequestsProcessor


class BrasilAPI:

    processor: RequestsProcessor

    def __init__(self, processor: RequestsProcessor = RequestsProcessor()):
        self.processor = processor

    def get_banks(self) -> list[Bank]:
        banks_response: dict = self.processor.get_data("/banks/v1")
        return [Bank.parse_obj(bank_item) for bank_item in banks_response]

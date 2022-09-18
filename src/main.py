from .entities import ApiRouteGet
from .adapters import RoutesAdapter
from .errors import RouteNotFoundError
from typing import Callable

API_BASE_URL = 'https://brasilapi.com.br/api'
API_GET_ROUTES = {
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
}


class BrasilApiClient(object):
    """Brasil API client."""

    def __init__(self) -> None:
        self.routes = RoutesAdapter.handle(API_BASE_URL, API_GET_ROUTES, ApiRouteGet)
    
    def __call__(self) -> None:
        for route in self.route:
            setattr(self, route.name, route.request)
    
    def __getattr__(self, name: str) -> Callable:
        """ route endpoint requester.
        Params:
            name <string>: endpoint name.

        Exceptions:
            RouteNotFoundError: throws when the called method do not exists.

        Returns <Callable>:
            method of the <IApiRoute>.
        """
        for route in self.routes:
            if route.name == name:
                return route.request
        
        raise RouteNotFoundError(f'route "{name}" do not exists.')

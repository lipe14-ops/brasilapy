from brasilapy.constants import APIVersion, FipeTipoVeiculo, IBGEProvider, TaxaJurosType
from brasilapy.models.cnpj import CNPJ
from brasilapy.models.general import (
    CEP,
    DDD,
    Bank,
    CEPv2,
    FeriadoNacional,
    FipePreco,
    FipeTabelaItem,
    FipeVeiculo,
    IbgeEstado,
    IbgeMunicipio,
    RegistroBrDominio,
    TaxaJuros,
)
from brasilapy.processor import RequestsProcessor


class BrasilAPI:

    processor: RequestsProcessor

    def __init__(self, processor_handler: RequestsProcessor = RequestsProcessor):
        self.processor = processor_handler()

    def get_banks(self) -> list[Bank]:
        banks = self.processor.get_data("/banks/v1")
        return [Bank.parse_obj(bank) for bank in banks]

    def get_bank(self, code: int) -> Bank:
        bank_response: dict = self.processor.get_data(f"/banks/v1/{code}")

        return Bank.parse_obj(bank_response)

    def get_cep(self, cep: str, api_version: APIVersion = APIVersion.V1) -> CEP | CEPv2:

        if len(cep) != 8:
            raise TypeError("Please provide a valid CEP number")

        if api_version not in [APIVersion.V1, APIVersion.V2]:
            raise TypeError("A valid API version must be provided for this call")

        model_class = CEP

        if api_version == APIVersion.V2:
            model_class = CEPv2

        cep_details: dict = self.processor.get_data(f"/cep/{api_version}/{cep}")

        return model_class.parse_obj(cep_details)

    def get_cnpj(self, cnpj: str) -> CNPJ:
        if len(cnpj) != 14:
            raise TypeError("Please provide a valid CNPJ number")

        cnpj_details: dict = self.processor.get_data(f"/cnpj/v1/{cnpj}")
        return CNPJ.parse_obj(cnpj_details)

    def get_ddd(self, ddd: str):
        if len(ddd) != 2:
            raise TypeError("Please provide a DDD number (2 digits)")

        ddd_details: dict = self.processor.get_data(f"/ddd/v1/{ddd}")
        return DDD.parse_obj(ddd_details)

    def get_feriados(self, year: int) -> list[FeriadoNacional]:
        feriados = self.processor.get_data(f"/feriados/v1/{year}")
        return [FeriadoNacional.parse_obj(feriado) for feriado in feriados]

    def get_fipe_veiculos(
        self,
        tipo_veiculo: FipeTipoVeiculo = FipeTipoVeiculo.CARROS,
        tabela_referencia: int | None = None,
    ) -> list[FipeVeiculo]:
        carros = self.processor.get_data(
            f"/fipe/marcas/v1/{tipo_veiculo}",
            params={"tabela_referencia": tabela_referencia}
            if tabela_referencia
            else None,
        )

        return [FipeVeiculo.parse_obj(carro) for carro in carros]

    def get_fipe_precos(
        self, codigo_fipe: str, tabela_referencia: int | None = None
    ) -> list[FipePreco]:
        precos = self.processor.get_data(
            f"/fipe/preco/v1/{codigo_fipe}",
            params={"tabela_referencia": tabela_referencia}
            if tabela_referencia
            else None,
        )
        return [FipePreco.parse_obj(preco) for preco in precos]

    def get_fipe_tabelas(self) -> list[FipeTabelaItem]:
        items = self.processor.get_data("/fipe/tabelas/v1/")
        return [FipeTabelaItem.parse_obj(item) for item in items]

    def get_ibge_municipios(
        self,
        state_uf: str,
        providers: tuple[IBGEProvider] = (
            IBGEProvider.DADOS_ABERTOS_BR,
            IBGEProvider.GOV,
            IBGEProvider.WIKIPEDIA,
        ),
    ) -> list[IbgeMunicipio]:

        if not providers:
            raise TypeError("A list of providers must be defined")

        if not state_uf:
            raise TypeError("A state must be defined")

        municipios = self.processor.get_data(
            f"/ibge/municipios/v1/{state_uf}", params={"providers": ",".join(providers)}
        )

        return [IbgeMunicipio.parse_obj(municipio) for municipio in municipios]

    def get_ibge_estados(self) -> list[IbgeEstado]:
        estados = self.processor.get_data("/ibge/uf/v1")
        return [IbgeEstado.parse_obj(estado) for estado in estados]

    def get_ibge_estado(self, state_uf: str) -> IbgeEstado:
        if not state_uf:
            raise TypeError("A UF must be defined")

        estado = self.processor.get_data(f"/ibge/uf/v1/{state_uf}")
        return IbgeEstado.parse_obj(estado)

    def get_registro_br_domain(self, fqdn: str) -> RegistroBrDominio:
        if not fqdn.endswith(".br"):
            raise ValueError("The domain must end with '.br'")

        registro_br_dominio = self.processor.get_data(f"/registrobr/v1/{fqdn}")

        registro_br_dominio["publication_status"] = registro_br_dominio[
            "publication-status"
        ]
        registro_br_dominio["expires_at"] = registro_br_dominio["expires-at"]

        del registro_br_dominio["publication-status"]
        del registro_br_dominio["expires-at"]

        return RegistroBrDominio.parse_obj(registro_br_dominio)

    def get_taxas_juros(self) -> list[TaxaJuros]:
        taxas = self.processor.get_data("/taxas/v1/")
        return [TaxaJuros.parse_obj(taxa) for taxa in taxas]

    def get_taxa_juros(self, taxa: TaxaJurosType) -> TaxaJuros:
        taxa = self.processor.get_data(f"/taxas/v1/{taxa}")
        return TaxaJuros.parse_obj(taxa)

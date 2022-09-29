from brasilapy.constants import APIVersion
from brasilapy.models.cnpj import CNPJ
from brasilapy.models.general import CEP, DDD, Bank, CEPv2, FeriadoNacional
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

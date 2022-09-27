from brasilapy.constants import APIVersion
from brasilapy.models import CEP, Bank, CEPv2
from brasilapy.processor import RequestsProcessor


class BrasilAPI:

    processor: RequestsProcessor

    def __init__(self, processor_handler: RequestsProcessor = RequestsProcessor):
        self.processor = processor_handler()

    def get_banks(self) -> list[Bank]:
        banks: dict = self.processor.get_data("/banks/v1")
        return [Bank.parse_obj(bank) for bank in banks]

    def get_bank(self, code: int) -> Bank:
        bank_response: dict = self.processor.get_data(f"/banks/v1/{code}")

        return Bank.parse_obj(bank_response)

    def get_cep(self, cep: str, api_version: APIVersion = APIVersion.V1) -> CEP | CEPv2:
        if api_version not in [APIVersion.V1, APIVersion.V2]:
            raise TypeError("A valid API version must be provided for this call")

        model_class = CEP

        if api_version == APIVersion.V2:
            model_class = CEPv2

        cep_details: dict = self.processor.get_data(f"/cep/{api_version}/{cep}")

        return model_class.parse_obj(cep_details)

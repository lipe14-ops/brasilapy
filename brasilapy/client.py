from brasilapy.models import Bank
from brasilapy.processor import RequestsProcessor


class BrasilAPI:

    processor: RequestsProcessor

    def __init__(self, processor_handler: RequestsProcessor = RequestsProcessor):
        self.processor = processor_handler()

    def get_banks(self) -> list[Bank]:
        banks_response: dict = self.processor.get_data("/banks/v1")
        return [Bank.parse_obj(bank_item) for bank_item in banks_response]

    def get_bank(self, code: int) -> Bank:
        bank_response: dict = self.processor.get_data(f"/banks/v1/{str(code)}")
        return Bank.parse_obj(bank_response)

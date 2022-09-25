from brasilapy.models import Bank
from brasilapy.processor import RequestsProcessor


class BrasilAPI:

    processor: RequestsProcessor

    def __init__(self, processor: RequestsProcessor = RequestsProcessor):
        self.processor = processor()

    def get_banks(self) -> list[Bank]:
        banks_response: dict = self.processor.get_data("/banks/v1")
        return [Bank.parse_obj(bank_item) for bank_item in banks_response]

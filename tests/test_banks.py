from unittest import mock

from brasilapy import BrasilAPI
from brasilapy.models import Bank


class TestBanks:
    def test_get_banks(self, brasil_api: BrasilAPI, request_banks_list_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=request_banks_list_json,
        ) as get_data_mock:

            banks = brasil_api.get_banks()

            get_data_mock.assert_called_once()

            assert len(banks) == len(request_banks_list_json)
            assert banks[0].dict() == request_banks_list_json[0]
            assert type(banks[0]) is Bank

    def test_get_bank(self, brasil_api: BrasilAPI, request_banks_list_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=request_banks_list_json[0],
        ) as get_data_mock:

            bank = brasil_api.get_bank(code=1)

            get_data_mock.assert_called_once()

            assert bank.dict() == request_banks_list_json[0]
            assert type(bank) is Bank

            assert bank.code == request_banks_list_json[0].get('code')
            assert bank.ispb == request_banks_list_json[0].get('ispb')
            assert bank.name == request_banks_list_json[0].get('name')
            assert bank.fullName == request_banks_list_json[0].get('fullName')

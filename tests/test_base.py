from unittest import mock

from brasilapy import BrasilAPI
from brasilapy.models import Bank


class TestBaseRequests:
    def test_get_banks(self, api_client, request_banks_dict):
        brasil_api: BrasilAPI = api_client

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=request_banks_dict,
        ) as get_data_mock:

            banks = brasil_api.get_banks()

            get_data_mock.assert_called_once()
            assert len(banks) == len(request_banks_dict)
            assert banks[0].dict() == request_banks_dict[0]
            assert type(banks[0]) is Bank

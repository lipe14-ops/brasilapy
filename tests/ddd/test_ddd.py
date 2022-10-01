from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.models.general import DDD


class TestDDD:
    def test_get_ddd_with_invalid_input(self, brasil_api: BrasilAPI):

        error_message = "Please provide a DDD number (2 digits)"

        with pytest.raises(TypeError) as exc1:
            brasil_api.get_ddd(ddd="1")

        with pytest.raises(TypeError) as exc2:
            brasil_api.get_ddd(ddd="083")

        assert error_message in str(exc1)
        assert error_message in str(exc2)

    def test_get_ddd_defaults(self, brasil_api: BrasilAPI, ddd_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=ddd_json,
        ) as get_data_mock:

            ddd_detail = brasil_api.get_ddd(ddd="99")

            get_data_mock.assert_called_once()

            assert ddd_detail.dict() == ddd_json
            assert type(ddd_detail) is DDD

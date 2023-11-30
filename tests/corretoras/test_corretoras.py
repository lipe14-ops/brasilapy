from datetime import datetime
from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.models.general import Corretora


class TestCorretoras:
    def test_get_corretoras_with_invalid_input(self, brasil_api: BrasilAPI):

        error_message = "Please provide a valid CNPJ number"

        with pytest.raises(TypeError) as exc1:
            brasil_api.get_corretoras(cnpj="1111155555999988")

        with pytest.raises(TypeError) as exc2:
            brasil_api.get_corretoras(cnpj="11111555559")

        assert error_message in str(exc1)
        assert error_message in str(exc2)

    def test_get_corretoras_defaults(self, brasil_api: BrasilAPI, corretoras_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=corretoras_json,
        ) as get_data_mock:

            corretora_detail = brasil_api.get_corretoras(cnpj="02332886000104")

            get_data_mock.assert_called_once()

            assert corretora_detail.dict() == corretoras_json
            assert type(corretora_detail) is Corretora
from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.models.cnpj import CNPJ


class TestCNPJ:
    def test_get_cnpj_with_invalid_input(self, brasil_api: BrasilAPI):
        with pytest.raises(TypeError) as exc1:
            brasil_api.get_cnpj(cnpj="1111155555999988")

        with pytest.raises(TypeError) as exc2:
            brasil_api.get_cnpj(cnpj="11111555559")

        assert "Please provide a valid CNPJ number" in str(exc1)
        assert "Please provide a valid CNPJ number" in str(exc2)

    def test_get_cnpj_with_defaults(self, brasil_api: BrasilAPI, cnpj_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=cnpj_json,
        ) as get_data_mock:

            cnpj_detail = brasil_api.get_cnpj(cnpj="11111000002222")

            get_data_mock.assert_called_once()

            assert cnpj_detail.dict() == cnpj_json
            assert type(cnpj_detail) is CNPJ

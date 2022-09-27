from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.constants import APIVersion
from brasilapy.models import CEP, CEPv2


class TestCEP:
    def test_get_cep_with_defaults(self, brasil_api: BrasilAPI, cep_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=cep_json,
        ) as get_data_mock:

            cep_detail = brasil_api.get_cep(cep="58000000")

            get_data_mock.assert_called_once()

            assert cep_detail.dict() == cep_json
            assert type(cep_detail) is CEP

    def test_get_cep_ensure_v1(self, brasil_api: BrasilAPI, cep_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=cep_json,
        ) as get_data_mock:

            cep_detail = brasil_api.get_cep(cep="58000000", api_version=APIVersion.V1)

            get_data_mock.assert_called_once()

            assert cep_detail.dict() == cep_json
            assert type(cep_detail) is CEP

    def test_get_cep_with_invalid_api_version(self, brasil_api: BrasilAPI):

        with pytest.raises(TypeError) as exp:
            brasil_api.get_cep(cep="58000000", api_version="v4")

        assert "A valid API version must be provided for this call" in str(exp)

    def test_get_cep_ensure_v2(self, brasil_api: BrasilAPI, cep_v2_json):
        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=cep_v2_json,
        ) as get_data_mock:

            cep_detail = brasil_api.get_cep(cep="58000000", api_version=APIVersion.V2)

            get_data_mock.assert_called_once()

            cep_v2_json["location"]["coordinates"]["longitude"] = float(
                cep_v2_json["location"]["coordinates"]["longitude"]
            )
            cep_v2_json["location"]["coordinates"]["latitude"] = float(
                cep_v2_json["location"]["coordinates"]["latitude"]
            )

            assert cep_detail.dict() == cep_v2_json
            assert type(cep_detail) is CEPv2

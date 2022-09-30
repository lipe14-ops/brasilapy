from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.models.general import IBGEItem


class TestIBGE:
    def test_get_ibge_municipios_invalid_payload(self, brasil_api: BrasilAPI):

        with pytest.raises(TypeError):
            brasil_api.get_ibge_municipios(state_uf=None)

        with pytest.raises(TypeError) as exc:
            brasil_api.get_ibge_municipios(state_uf="pb", providers=None)

        assert "A list of providers must be defined" in str(exc)

    def test_get_ibge_municipios(self, brasil_api: BrasilAPI, ibge_municipios_json):
        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=ibge_municipios_json,
        ) as get_data_mock:

            ibge_municipios = brasil_api.get_ibge_municipios(state_uf="pb")

            get_data_mock.assert_called_once()

            assert ibge_municipios[0].dict() == ibge_municipios[0]
            assert type(ibge_municipios[0]) is IBGEItem

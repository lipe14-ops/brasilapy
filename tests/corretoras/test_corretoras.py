from unittest import mock

from brasilapy import BrasilAPI
from brasilapy.models.general import Corretoras


class TestCorretoras:
    def test_corretoras(self, brasil_api: BrasilAPI, request_example_list):
        with mock.patch('brasilapy.client.RequestsProcessor.get_data', return_value=request_example_list) as mock_get:
            corretoras = brasil_api.get_corretoras()
            mock_get.assert_called_once()
            assert corretoras[0].nome_comercial == "XP INVESTIMENTOS"
            assert dict(corretoras[0]) == request_example_list[0]
            assert type(corretoras[0]) == Corretoras

    def test_get_corretora(self, brasil_api: BrasilAPI, request_example_list):
        with mock.patch('brasilapy.client.RequestsProcessor.get_data', return_value=request_example_list[0]) as mock_get:
            corretora = brasil_api.get_corretora(request_example_list[0]['cnpj'])
            mock_get.assert_called_once()
            assert corretora.nome_comercial == "XP INVESTIMENTOS"
            assert dict(corretora) == request_example_list[0]
            assert type(corretora) == Corretoras
            assert corretora.cnpj == request_example_list[0]['cnpj']
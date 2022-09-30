from unittest import mock

from brasilapy import BrasilAPI
from brasilapy.models.general import FipePreco, FipeTabelaItem, FipeVeiculo


class TestFipe:
    def test_fipe_veiculos(self, brasil_api: BrasilAPI, fipe_veiculos_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=fipe_veiculos_json,
        ) as get_data_mock:

            fipe_veiculos = brasil_api.get_fipe_veiculos()

            get_data_mock.assert_called_once()

            fipe_veiculos_json[0]["valor"] = int(fipe_veiculos_json[0]["valor"])

            assert fipe_veiculos[0].dict() == fipe_veiculos_json[0]
            assert type(fipe_veiculos[0]) is FipeVeiculo

    def test_fipe_precos(self, brasil_api: BrasilAPI, fipe_precos_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=fipe_precos_json,
        ) as get_data_mock:

            fipe_precos = brasil_api.get_fipe_precos(codigo_fipe="0012345")

            get_data_mock.assert_called_once()

            assert fipe_precos[0].dict() == fipe_precos_json[0]
            assert type(fipe_precos[0]) is FipePreco

    def test_fipe_tabela(self, brasil_api: BrasilAPI, fipe_tabelas_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=fipe_tabelas_json,
        ) as get_data_mock:

            fipe_tabelas = brasil_api.get_fipe_tabelas()

            get_data_mock.assert_called_once()

            assert fipe_tabelas[0].dict() == fipe_tabelas_json[0]
            assert type(fipe_tabelas[0]) is FipeTabelaItem

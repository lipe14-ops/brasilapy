from unittest import mock
from datetime import datetime

from brasilapy import BrasilAPI
from brasilapy.models.general import NCM


class TestNCM:

    def test_get_ncms(self, brasil_api: BrasilAPI, ncm_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=ncm_json,
        ) as get_data_mock:

            ncms = brasil_api.get_ncms()

            get_data_mock.assert_called_once()

            ncm_json[0]["data_inicio"] = datetime.strptime(
                ncm_json[0]["data_inicio"], "%Y-%m-%d"
            ).date()

            ncm_json[0]["data_fim"] = datetime.strptime(
                ncm_json[0]["data_fim"], "%Y-%m-%d"
            ).date()

            assert len(ncms) == len(ncm_json)
            assert ncms[0].dict() == ncm_json[0]
            assert type(ncms[0]) is NCM

            assert ncms[0].codigo == ncm_json[0].get("codigo")
            assert ncms[0].descricao == ncm_json[0].get("descricao")
            assert ncms[0].data_inicio == ncm_json[0].get("data_inicio")
            assert ncms[0].data_fim == ncm_json[0].get("data_fim")
            assert ncms[0].tipo_ato == ncm_json[0].get("tipo_ato")
            assert ncms[0].numero_ato == ncm_json[0].get("numero_ato")
            assert ncms[0].ano_ato == ncm_json[0].get("ano_ato")

    def test_get_ncm(self, brasil_api: BrasilAPI, ncm_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=ncm_json[0],
        ) as get_data_mock:

            ncm = brasil_api.get_ncm(codigo="01")

            get_data_mock.assert_called_once()

            ncm_json[0]["data_inicio"] = datetime.strptime(
                ncm_json[0]["data_inicio"], "%Y-%m-%d"
            ).date()

            ncm_json[0]["data_fim"] = datetime.strptime(
                ncm_json[0]["data_fim"], "%Y-%m-%d"
            ).date()

            assert ncm.dict() == ncm_json[0]
            assert type(ncm) is NCM
            
            assert ncm.codigo == ncm_json[0].get("codigo")
            assert ncm.descricao == ncm_json[0].get("descricao")
            assert ncm.data_inicio == ncm_json[0].get("data_inicio")
            assert ncm.data_fim == ncm_json[0].get("data_fim")
            assert ncm.tipo_ato == ncm_json[0].get("tipo_ato")
            assert ncm.numero_ato == ncm_json[0].get("numero_ato")
            assert ncm.ano_ato == ncm_json[0].get("ano_ato")

    def test_ncm_descricao(self, brasil_api: BrasilAPI, ncm_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=ncm_json,
        ) as get_data_mock:

            ncms = brasil_api.get_ncm_descricao(descricao="Animais vivos.")

            get_data_mock.assert_called_once()

            ncm_json[0]["data_inicio"] = datetime.strptime(
                ncm_json[0]["data_inicio"], "%Y-%m-%d"
            ).date()

            ncm_json[0]["data_fim"] = datetime.strptime(
                ncm_json[0]["data_fim"], "%Y-%m-%d"
            ).date()

            assert len(ncms) == len(ncm_json)
            assert type(ncms[0]) is NCM
            
            assert ncms[0].codigo == ncm_json[0].get("codigo")
            assert ncms[0].descricao == ncm_json[0].get("descricao")
            assert ncms[0].data_inicio == ncm_json[0].get("data_inicio")
            assert ncms[0].data_fim == ncm_json[0].get("data_fim")
            assert ncms[0].tipo_ato == ncm_json[0].get("tipo_ato")
            assert ncms[0].numero_ato == ncm_json[0].get("numero_ato")
            assert ncms[0].ano_ato == ncm_json[0].get("ano_ato")

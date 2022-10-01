from datetime import datetime
from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.exceptions import ProcessorException
from brasilapy.models.general import FeriadoNacional


class TestFeriados:
    def test_get_feriado_with_invalid_input(
        self, brasil_api: BrasilAPI, feriados_request_404_response_text
    ):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            side_effect=ProcessorException(
                status_code=404, response_text=feriados_request_404_response_text
            ),
        ), pytest.raises(ProcessorException):
            brasil_api.get_feriados(year=1800)

    def test_get_feriados_defaults(self, brasil_api: BrasilAPI, feriados_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=feriados_json,
        ) as get_data_mock:

            feriados = brasil_api.get_feriados(year=2022)

            get_data_mock.assert_called_once()

            feriados_json[0]["date"] = datetime.strptime(
                feriados_json[0]["date"], "%Y-%m-%d"
            ).date()

            assert feriados[0].dict() == feriados_json[0]
            assert type(feriados[0]) is FeriadoNacional

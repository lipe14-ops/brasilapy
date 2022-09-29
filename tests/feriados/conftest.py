import json

import pytest


@pytest.fixture
def feriados_json():
    return [
        {"date": "2022-01-01", "name": "Confraternização mundial", "type": "national"},
        {"date": "2022-03-01", "name": "Carnaval", "type": "national"},
        {"date": "2022-04-15", "name": "Sexta-feira Santa", "type": "national"},
        {"date": "2022-04-17", "name": "Páscoa", "type": "national"},
        {"date": "2022-04-21", "name": "Tiradentes", "type": "national"},
        {"date": "2022-05-01", "name": "Dia do trabalho", "type": "national"},
        {"date": "2022-06-16", "name": "Corpus Christi", "type": "national"},
        {"date": "2022-09-07", "name": "Independência do Brasil", "type": "national"},
        {"date": "2022-10-12", "name": "Nossa Senhora Aparecida", "type": "national"},
        {"date": "2022-11-02", "name": "Finados", "type": "national"},
        {"date": "2022-11-15", "name": "Proclamação da República", "type": "national"},
        {"date": "2022-12-25", "name": "Natal", "type": "national"},
    ]


@pytest.fixture
def feriados_request_404_response_text():
    return json.dumps(
        {
            "message": "Ano fora do intervalo suportado entre 1900 e 2199.",
            "type": "feriados_range_error",
            "name": "NotFoundError",
        }
    )

import pytest


@pytest.fixture
def ibge_municipios_json():
    return [
        {"nome": "ÁGUA BRANCA", "codigo_ibge": "2500106"},
        {"nome": "AGUIAR", "codigo_ibge": "2500205"},
        {"nome": "ALAGOA GRANDE", "codigo_ibge": "2500304"},
        {"nome": "ALAGOA NOVA", "codigo_ibge": "2500403"},
        {"nome": "ALAGOINHA", "codigo_ibge": "2500502"},
    ]


@pytest.fixture
def ibge_estados_json():
    return [
        {
            "id": 11,
            "sigla": "RO",
            "nome": "Rondônia",
            "regiao": {"id": 1, "sigla": "N", "nome": "Norte"},
        },
        {
            "id": 12,
            "sigla": "AC",
            "nome": "Acre",
            "regiao": {"id": 1, "sigla": "N", "nome": "Norte"},
        },
        {
            "id": 13,
            "sigla": "AM",
            "nome": "Amazonas",
            "regiao": {"id": 1, "sigla": "N", "nome": "Norte"},
        },
        {
            "id": 14,
            "sigla": "RR",
            "nome": "Roraima",
            "regiao": {"id": 1, "sigla": "N", "nome": "Norte"},
        },
    ]

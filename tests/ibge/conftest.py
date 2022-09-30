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

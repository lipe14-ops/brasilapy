import pytest


@pytest.fixture
def taxas_json():
    return [
        {"nome": "Selic", "valor": 13.75},
        {"nome": "CDI", "valor": 13.65},
        {"nome": "IPCA", "valor": 8.73},
    ]

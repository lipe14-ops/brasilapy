import pytest


@pytest.fixture
def cep_json():
    return {
        "cep": "58000000",
        "state": "XX",
        "city": "City Name",
        "neighborhood": "Neighborhood Name",
        "street": "Some Street Name",
        "service": "correios",
    }


@pytest.fixture
def cep_v2_json():
    return {
        "cep": "58000000",
        "state": "XX",
        "city": "City Name",
        "neighborhood": "Neighborhood",
        "street": "Rua Benício de Oliveira Lima",
        "service": "correios",
        "location": {
            "type": "Point",
            "coordinates": {"longitude": "-35.8302959", "latitude": "-4.0134576"},
        },
    }

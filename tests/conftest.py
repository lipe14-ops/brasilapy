import pytest
from brasilapy import BrasilAPI


@pytest.fixture
def api_client():
    return BrasilAPI()


@pytest.fixture
def request_banks_dict():
    return [
        {
            "ispb": "00000000",
            "name": "BCO DO BRASIL S.A.",
            "code": 1,
            "fullName": "Banco do Brasil S.A."
        },
        {
            "ispb": "00000208",
            "name": "BRB - BCO DE BRASILIA S.A.",
            "code": 70,
            "fullName": "BRB - BANCO DE BRASILIA S.A."
        },
        {
            "ispb": "00038121",
            "name": "Selic",
            "code": None,
            "fullName": "Banco Central do Brasil - Selic"
        },
        {
            "ispb": "00038166",
            "name": "Bacen",
            "code": None,
            "fullName": "Banco Central do Brasil"
        }
    ]
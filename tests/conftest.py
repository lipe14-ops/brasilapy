import pytest

from brasilapy import BrasilAPI


@pytest.fixture
def brasil_api():
    return BrasilAPI()

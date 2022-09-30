from datetime import datetime
from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.models.general import RegistroBrDominio


class TestRegistroBr:
    def test_get_registro_domain_with_invalid_input(self, brasil_api: BrasilAPI):

        with pytest.raises(ValueError):
            brasil_api.get_registro_br_domain(fqdn="google.com")

    def test_get_domain(self, brasil_api: BrasilAPI, registro_br_domain_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=registro_br_domain_json,
        ):

            registro_br = brasil_api.get_registro_br_domain(fqdn="test.com.br")

            assert type(registro_br.expires_at) is datetime
            assert type(registro_br) is RegistroBrDominio

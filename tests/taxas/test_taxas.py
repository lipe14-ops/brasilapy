from unittest import mock

from brasilapy import BrasilAPI
from brasilapy.constants import TaxaJurosType
from brasilapy.models.general import TaxaJuros


class TestTaxas:
    def test_get_taxas(self, brasil_api: BrasilAPI, taxas_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=taxas_json,
        ):

            taxas = brasil_api.get_taxas_juros()

            assert type(taxas[0]) is TaxaJuros
            assert taxas[0].dict() == taxas_json[0]

    def test_taxa_per_type(self, brasil_api: BrasilAPI, taxas_json):

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=taxas_json[0],
        ):

            taxa = brasil_api.get_taxa_juros(taxa_nome=TaxaJurosType.SELIC)

            assert type(taxa) is TaxaJuros
            assert taxa.dict() == taxas_json[0]

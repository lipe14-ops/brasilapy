import pytest


@pytest.fixture
def ncm_json():
    return [
        {
            "codigo":"01",
            "descricao":"Animais vivos.",
            "data_inicio":"2022-04-01",
            "data_fim":"9999-12-31",
            "tipo_ato":"Res Camex",
            "numero_ato":"000272",
            "ano_ato":"2021"
        },
        {
            "codigo":"01.01",
            "descricao":"Cavalos, asininos e muares, vivos.",
            "data_inicio":"2022-04-01",
            "data_fim":"9999-12-31",
            "tipo_ato":"Res Camex",
            "numero_ato":"000272",
            "ano_ato":"2021"
        },
        {
            "codigo":"0101.2",
            "descricao":"- Cavalos:",
            "data_inicio":"2022-04-01",
            "data_fim":"9999-12-31",
            "tipo_ato":"Res Camex",
            "numero_ato":"000272",
            "ano_ato":"2021"
        }
    ]

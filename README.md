![](./images/brasilapi-logo-small.png) <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="70" height="70" /> 

# BrasilApy
Um cliente da [Brasil  API](https://brasilapi.com.br/) em python3. E aqui vai o [repositório](https://github.com/BrasilAPI/BrasilAPI) oficial.

## Instalação:
rode o comando `pip install brasilapy` e estará tudo pronto.
## Documentação:
Documentação oficial da [API](https://brasilapi.com.br/docs).

### um código simples de exemplo
```py
from brasilapy import BrasilApiClient

#acesse os endpoints pela variável client. 
client = BrasilApiClient()
response = client.get_estado('GO', {})

print(response.content) #imprime o response da API.
```

### atributos do `BrasilApiClient`

| metodos do cliente    |  endpoint da API |
|:------------:|:------------------:| 
|   get_banks | /banks/v1/ |
| get_bank | /banks/v1/{code}
| get_cep_v1| /cep/v1/{cep}
|get_cep_v2| /cep/v2/{cep}
|get_cnpj  | /cnpj/v1/{cnpj}
|get_ddd   | /ddd/v1/{ddd}
|get_feriados_nacionais| /feriados/v1/{ano}
|get_fipe_veiculo | /fipe/marcas/v1/{tipoVeiculo}
|get_fipe_precos | /fipe/preco/v1/{codigoFipe}
|get_fipe_tabelas| /banks/v1/
|get_ibge_municipios| /ibge/municipios/v1/{siglaUF}?providers=dados-abertos-br,gov,wikipedia
|get_ibge_estados| /ibge/uf/v1
|get_ibge_estado| /ibge/uf/v1/{code}
| get_registro_br| /regsitrobr/v1/{domain}
| get_taxas | /taxas/v1
| get_taxa | /taxas/v1/{sigla}

### O response possue 3 atributos:

| atributo | descrição |
|:--------:|:---------:|
|header| header http |
|status| http status code|
|content| API json body |

## autor
<img width='100' height='100' style="border-radius:50%; padding:15px" src="https://avatars.githubusercontent.com/u/78698099?v=4" /></br>
<a href="https://github.com/lipe14-ops" style='padding: 15px' title="Rocketseat">Filipe Soares :computer:</a>
<p style='padding: 15px'>made with :heart: by <strong>Filipe</strong> :wave: reach me!!!</p>


[![](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](fn697169@gmail.com)
[![](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/filipe_1408/)
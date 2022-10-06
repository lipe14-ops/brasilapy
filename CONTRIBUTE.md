# Contribuindo com o repositório

Se voce chegou a esse link, muito obrigado! Nós apreciamos todo o tipo de ajuda para tornar essa biblioteca cada vez melhor.
Este guia visa mostrar como iniciar, rodar, testar e preparar esse projeto para um merge bem sucedido.

## Como contribuir?

### Requisitos
Para trabalhar com o projeto voce precisa do seguinte conjunto ferramental:
* Python 3.10+; (inicialmente suportamos apenas a última versão disponível do python);
  * Caso queira, voce pode usar um gerenciador de dependencias python. Recomendamos o [Pyenv](https://github.com/pyenv/pyenv). Ele conversa bem com o Poetry;
* [Poetry](https://python-poetry.org/) (Responsável por gerenciar o projeto, servindo de ponte de comunicação com o PyPI)

### Primeiro setup
1. Uma vez que voce clonou o projeto instale as dependencias para começar o trabalho;


    $ poetry install --with dev

    Creating virtualenv brasilapy-L06DoqL8-py3.10 in /Users/jon/Library/Caches/pypoetry/virtualenvs
    Installing dependencies from lock file

    Package operations: 31 installs, 1 update, 0 removals

    • Installing pyparsing (3.0.9)
    • Installing attrs (22.1.0)
    • Installing distlib (0.3.6)
    • Installing filelock (3.8.0)
    • Installing iniconfig (1.1.1)
    • Installing packaging (21.3)
    • Installing platformdirs (2.5.2)
    • Installing pluggy (1.0.0)
    • Installing py (1.11.0)
    • Updating setuptools (65.3.0 -> 65.4.0)
    • Installing tomli (2.0.1)
    • Installing certifi (2022.9.24): Installing...
    • Installing cfgv (3.3.1): Installing...
    • Installing certifi (2022.9.24)
    • Installing cfgv (3.3.1)
    • Installing charset-normalizer (2.1.1)
    • Installing coverage (6.4.4)
    • Installing identify (2.5.5)
    • Installing idna (3.4)
    • Installing mypy-extensions (0.4.3)
    • Installing nodeenv (1.7.0)
    • Installing pytest (7.1.3)
    • Installing pyyaml (6.0)
    • Installing toml (0.10.2)
    • Installing types-urllib3 (1.26.25)
    • Installing typing-extensions (4.3.0)
    • Installing urllib3 (1.26.12)
    • Installing virtualenv (20.16.5)
    • Installing mypy (0.982)
    • Installing pre-commit (2.20.0)
    • Installing pydantic (1.10.2)
    • Installing pytest-cov (3.0.0)
    • Installing requests (2.28.1)
    • Installing types-requests (2.28.11)

    Installing the current project: brasilapy (1.2.0)

2. Instale o wrapper do `pre-commit`. Ele te ajudará a verificar seu código antes de cada commit. Caso tenha curiosidade sobre o projeto, voce pode achar no site oficial em [https://pre-commit.com/](https://pre-commit.com/).


    $ poetry shell  # Isso entra dentro do virtualenv, onde o pre-commit está.
    Spawning shell within /Users/jon/Library/Caches/pypoetry/virtualenvs/brasilapy-L06DoqL8-py3.10

    (brasilapy-py3.10) $ pre-commit install
    pre-commit installed at .git/hooks/pre-commit


3. Agora só apontar para sua IDE favorita e voce está pronto para iniciar os trabalhos. =)

### Rodando testes

Para testar o projeto, é bem simples. Uma vez que voce estiver com o virtual environment do projeto ativado, rode o seguinte comando


    $ poetry shell  # Isso ativa o shell do python para o virtual environment
    (brasilapy-py3.10) $ pytest --cov
    ====================================== test session starts ======================================
    platform darwin -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
    rootdir: /Users/jon/Developer/opensource/brasilapi_testing
    plugins: cov-3.0.0
    collected 31 items

    tests/test_processor.py ....                                                              [ 12%]
    tests/test_utils.py ..                                                                    [ 19%]
    tests/banks/test_banks.py ..                                                              [ 25%]
    tests/cep/test_cep.py .....                                                               [ 41%]
    tests/cnpj/test_cnpj.py ..                                                                [ 48%]
    tests/ddd/test_ddd.py ..                                                                  [ 54%]
    tests/feriados/test_feriados.py ..                                                        [ 61%]
    tests/fipe/test_fipe.py ...                                                               [ 70%]
    tests/ibge/test_ibge.py .....                                                             [ 87%]
    tests/registro_br/test_registro_br.py ..                                                  [ 93%]
    tests/taxas/test_taxas.py ..                                                              [100%]

    ---------- coverage: platform darwin, python 3.10.6-final-0 ----------
    Name                          Stmts   Miss  Cover
    -------------------------------------------------
    brasilapy/__init__.py             1      0   100%
    brasilapy/client.py              76      0   100%
    brasilapy/constants.py           15      0   100%
    brasilapy/exceptions.py           7      0   100%
    brasilapy/models/cnpj.py         69      0   100%
    brasilapy/models/general.py      75      0   100%
    brasilapy/processor.py           18      0   100%
    brasilapy/utils.py                3      0   100%
    -------------------------------------------------
    TOTAL                           264      0   100%


    ====================================== 31 passed in 0.10s =======================================

### Criando um PR

1. Uma vez que voce está no projeto, crie uma branch com a funcionalidade que deseja desenvolver. Não possuimos um padrão, mas acho que seria bom utilizarmos uma notação para as branches da seguinte forma:

* feature/add_some_feature
* bugfix/fix_something_on_a_feature

2. Crie e ou edite os arquivos normalmente.
3. Adicione os arquivos e faça o `commit` de acordo. O pre-commit irá executar e validar seu commit.
   a. Caso queira, voce pode rodar o precommit manualmente usando `pre-commit run --all-files`.

4. Ao fazer o push para seu repositório, só criar um PR, descrever o que voce gostaria de resolver ou adicionar e aguardar pelas pipelines de validação serem executadas.

## Dúvidas?
Caso ainda reste alguma dúvida, só criar uma Issue que iremos ajudá-lo.
Obrigado e aguardamos suas contribuições. =)

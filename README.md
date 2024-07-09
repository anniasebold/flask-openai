## Descrição

API Desenvolvida com integração a OpenAI para responder a perguntas feitas por usuários.

## Pré requisitos

- Python 3.10
- Pip

## Clonando o repositório

Clone o repositório

```bash
git clone git@github.com:anniasebold/flask-openai.git
```

## Configuração do ambiente virtual

Criação do venv

```bash
python3 -m venv .venv
```

Ativação do ambiente virtual

```bash
source .venv/bin/activate
```

## Instalação das dependências

```bash
$ pip install -r requirements.txt
```

## Configuração das variáveis de ambiente

Criação do arquivo .env

```bash
$ touch .env
```

Por ser um conteúdo sensível, peça ao administrador do repositório o conteúdo do .env e cole no arquivo criado.

## Executando a aplicação

Na raíz do projeto:
```bash
$ python3 run.py
```

## Testes unitários

```bash
# unit tests
$ pytest

# unit tests cases
$ pytest -s -v 
```
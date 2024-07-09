## Descrição

API Desenvolvida com integração a OpenAI para responder a perguntas feitas por usuários.

## Clonando o repositório

Clone o repositório

```bash
git clone git@github.com:anniasebold/flask-openai.git
```

## Configuração das variáveis de ambiente

Criação do arquivo .env

```bash
$ touch .env
```

Por ser um conteúdo sensível, peça ao **administrador** do repositório o conteúdo do .env e cole no arquivo criado.

## Configuração do ambiente

### Pré requisitos

- docker
- docker-compose

Para realizar a configuração do ambiente é necessário o docker e o docker-compose instalados previamente.

Na primeira vez executando é necessário subir o docker com o build

```bash
docker-compose --build
```

Após isso suba a aplicação
```bash
docker-compose up web
```

A partir da primeira execução o --build não é mais necessário.

## Utilização da aplicação

A aplicação estará disponível: http://127.0.0.1:5000

Exemplo de uso:

```bash
curl --location --request POST 'http://localhost:5000/api/ecommerce/v1/question-and-answer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "question": "qual a melhor ração para golden?"
}'
```

## Testes unitários

Execução dos testes unitários:
```bash
$ docker-compose run tests pytest
```

Execução dos teste unitários detalhados:
```bash
$ docker-compose run tests pytest -s -v
```

## Configuração do ambiente virtual (opcional)

### Pré requisitos

- Python 3.9
- pip

Se você não quiser utilizar o Docker e quiser construir o ambiente na sua máquina é necessário o Python e o pip instalados previamente.

Criação do venv

```bash
python3 -m venv .venv
```

Ativação do ambiente virtual

```bash
source .venv/bin/activate
```

Instalação das dependências

```bash
$ pip install -r requirements.txt
```

Execução da aplicação

```bash
$ python3 run.py
```
Execução dos testes unitários
```bash
$ pytest
```

Execução dos teste unitários detalhados:
```bash
$ pytest -s -v
```
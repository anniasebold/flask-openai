## 📋 Descrição

API Desenvolvida com integração a OpenAI para responder a perguntas feitas por usuários.

## 💻 Tecnologias utilizadas

- **Flask**: Framework para a criação de APIs web.
- **OpenAI**: Plataforma de IA para processamento de perguntas e respostas.
- **pytest**: Ferramenta de testes unitários para garantir a qualidade do código.
- **pylint**: Ferramenta de análise de código estático para padronização e boas práticas.
- **Docker**: Plataforma de contêineres para criar, distribuir e executar aplicações.
- **Docker Compose**: Ferramenta para orquestração de aplicações multi-contêiner.

Essas foram as tecnologias utilizadas para construção da aplicação de forma que ela fosse escalável, bem testada e fácil de configurar.

# 💾 Como utilizar

## Clonando o repositório

```bash
git clone git@github.com:anniasebold/flask-openai.git
```

## Configuração das variáveis de ambiente

Criação do arquivo .env

```bash
touch .env
```
Dentro terão duas variáveis de ambiente:

```bash
OPENAI_API_KEY=openai_api_key_example
OPENAI_ORGANIZATION_ID=openai_organization_id_example
```

Se você tiver um token da OpenAI disponível e um Organization ID insira no .env criado.

Se não tiver, peça ao **administrador** do repositório o conteúdo do .env e cole no arquivo criado (por ser um conteúdo sensível não foi disponibilizado aqui).

## Configuração do ambiente

### Pré requisitos

- docker
- docker-compose

Para realizar a configuração do ambiente é necessário o docker e o docker-compose instalados previamente.

Na primeira vez executando é necessário rodar o build

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
docker-compose run tests pytest
```

Execução dos teste unitários detalhados:
```bash
docker-compose run tests pytest -s -v
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
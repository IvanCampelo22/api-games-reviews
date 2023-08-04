## Tecnologias usadas

* Python
* FastApi
* Alembic
* Docker
* Postgres
* AWS

## Como executar o projeto
1. Ir até a pasta do projeto e instale a virtualenv

> virtualenv venv

2. Ative a virtualenv

> source venv/bin/activate

3. Instale as dependencias

> pip install -r requirements.txt

4. Vá até a raiz do projeto e inicie o servidor

>  uvicorn main:app --reload

* Teste local

> http://127.0.0.1:8000/docs

## Como fazer migrações no banco de dados

1. Execute o comando para criar o arquivo de migração no versions

> alembic revision -m "<nome-da-migraçao>"

2. Depois de criada a migração execute

> alembic upgrade head --sql

> alembic upgrade head

### Obs: consulte a documentação do alembic para entender como fazer a migração no banco de dados, pois se trata de algo um tanto complexo
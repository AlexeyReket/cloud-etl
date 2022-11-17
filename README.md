# Rates Parser service

Project includes

* API. Implements working with users, manual trigger of cloud function and accessing to already parsed date
* Function. Implements parsing and saving data to database

## Get started with api

Create and activate virtualenv

```shell
virtualenv .venv
source .venv/bin/activate
```

Install dependencies

```shell
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
poetry install
```

Start db in compose

```shell
make compose-up
```

Create .env file from templated

```shell
cp env/.env.template env/.env
```

Config db connection url in `env/.env` and after apply migrations

```shell
make migrate
```

start app

```shell
make debug
```

# Environment variables

## API

#### ENVIRONMENT

> Specification of current working environment
>
> Default:
> > dev

#### API_KEY

> Key to access to cloud function

#### YANDEXCLOUD_TOKEN

> OAUTH token to access to cloud

#### DATABASE_URI

> Uri for access to database
>
> Example:
> > postgresql+asyncpg://db_user:db_password@db_host:5432/db_name

#### DATABASE_SCHEMA

> Database schema which will be used in queries

#### FUNCTION_URL

> URL to access to cloud function

#### SECRET_KEY

> Key for JWT tokens generation/verification

#### ALLOWED_ORIGINS

> CORS allowed origins
>
> Default:
> > ["*"]

#### ALLOWED_METHODS

> CORS allowed methods
>
> Default:
> > ["*"]

#### ALLOWED_HEADERS

> CORS allowed headers
>
> Default:
> > ["*"]

## function

#### DATABASE_SCHEMA

> Database schema which will be used in queries

#### API_KEY

> Will be used to authorize accessing

#### DB_DATABASE

> database name

#### DB_USER

> database name

#### DB_PASSWORD

> database password

#### DB_HOST

> database host

#### DB_PORT

> database port

# Deployment
## API
Build and push docker image

```shell
export registry_id="you registry_id"
make build
make push
```
## Function

Create zip 
```shell
make build-function
```
In project root will be created zip with all needed files

You can create function in cloud using this zip
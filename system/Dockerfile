FROM python:3.9.7-slim as base

WORKDIR api-v3000

RUN pip install -U poetry pip setuptools \
    && poetry config virtualenvs.create false

COPY system/start-server /usr/local/bin/
RUN chmod 777 /usr/local/bin/start-server

COPY pyproject.toml ./
RUN poetry install --only main

########################

FROM base

COPY app app

ENTRYPOINT ["start-server"]

FROM python:3.9-slim

WORKDIR /app

COPY poetry.lock /app
COPY pyproject.toml /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . /app
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml /app/

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi


COPY . /app


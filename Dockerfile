FROM python:3.9.12
ARG POETRY_VERSION=1.1.13
RUN pip install poetry=="$POETRY_VERSION"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /app

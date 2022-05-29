FROM python:3.10.4-slim-buster as build-base

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=/opt/poetry

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev


FROM build-base as development

RUN poetry install

EXPOSE 8000
CMD ["poetry", "run", "/app/manage.py", "runserver", "0:8000"]


FROM build-base as production

COPY ./ /app/

EXPOSE 8000
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi", "-w", "3"]


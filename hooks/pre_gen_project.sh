#!/bin/bash -e

echo Generating .env file...

echo POSTGRES_PASSWORD="{{ cookiecutter.ENV_DB_PASSWORD }}" > .env
echo POSTGRES_DB="{{ cookiecutter.ENV_DB_NAME }}" >> .env
echo POSTGRES_USER="{{ cookiecutter.ENV_DB_USER }}" >> .env
echo PGDATA=/var/lib/postgresql/data/pgdata >> .env

echo SECRET_KEY="{{ cookiecutter.ENV_SECRET_KEY }}" >> .env
echo DEBUG="{{ cookiecutter.ENV_DEBUG }}" >> .env
echo ALLOWED_HOSTS="{{ cookiecutter.ENV_DJANGO_ALLOWED_HOSTS }}" >> .env
echo DJANGO_STATIC_ROOT="{{ cookiecutter.ENV_DJANGO_STATIC_ROOT }}" >> .env
echo DATABASE_URL="psql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@{{ cookiecutter.ENV_DB_HOST }}:5432/${POSTGRES_DB}" >> .env

{% if cookiecutter.use_sentry == "yes" %}echo  SENTRY_DSN="{{ cookiecutter.ENV_SENTRY_DSN }}" >> .env {% endif %}

echo Done

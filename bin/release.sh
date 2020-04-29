#!/usr/bin/env bash

pipenv install django
pipenv install psycopg2-binary
pipenv run python manage.py migrate --noinput

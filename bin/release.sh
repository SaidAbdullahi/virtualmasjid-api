#!/usr/bin/env bash

pipenv install django
pipenv run python manage.py migrate --noinput

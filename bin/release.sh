#!/usr/bin/env bash

pipenv install django
pipenv install psycopg2==2.8.3 
pipenv run python manage.py migrate

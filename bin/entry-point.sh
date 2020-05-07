#!/usr/bin/env bash

gunicorn virtual_masjid.wsgi --log-file - & celery -A virtual_masjid worker -l info -c 2 --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -O fair

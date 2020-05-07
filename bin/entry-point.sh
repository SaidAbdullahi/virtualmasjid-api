#!/usr/bin/env bash

gunicorn virtual_masjid.wsgi --log-file - & celery -A virtual_masjid worker -l info -c 2

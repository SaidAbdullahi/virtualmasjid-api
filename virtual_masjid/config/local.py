import os
from .common import Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('dbname'),
        'USER': os.environ.get('dbuser'),
        'PASSWORD': os.environ.get('dbpass'),
        'HOST': os.environ.get('dbhost'),
        'PORT': os.environ.get('dbport')
        }
    }

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # CORS!
    CORS_ORIGIN_WHITELIST = (
        'https://localhost:8000',
    )

    CACHES = {
      'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
      }
    }

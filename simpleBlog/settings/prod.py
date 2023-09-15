from os import environ
from .base import *


SECRET_KEY = environ.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "simple_blog",
        "USER": "postgres",
        "PASSWORD": "mysecretpassword",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# EMAIL

HCAPTCHA_SITEKEY = environ.get("HCAPTCHA_SITEKEY")

HCAPTCHA_SECRET = environ.get("HCAPTCHA_SECRET")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": environ.get("DJANGO_LOG_LEVEL", "WARNING"),
        },
    },
    "formatters": {
        "verbose": {
            "format": "{asctime} ({levelname}) - {name} - {message}",
            "style": "{",
        }
    },
}

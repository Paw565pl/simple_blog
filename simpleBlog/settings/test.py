from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-73c&#%_6y4@l8u159!+#p7e##kewyf#3(022*=e)%x(tfcr4qr"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "simple_blog",
        "USER": "postgres",
        "PASSWORD": "mysecretpassword",
        "HOST": "db",
        "PORT": "5432",
    }
}

EMAIL_PORT = 1025

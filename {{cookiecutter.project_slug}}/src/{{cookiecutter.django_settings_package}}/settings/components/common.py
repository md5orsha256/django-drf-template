from pathlib import Path
from typing import List

from environ import Env


BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(BASE_DIR.parent.joinpath(".env").__str__())

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS: List[str] = env.list("ALLOWED_HOSTS", default=[])

ROOT_URLCONF = "{{cookiecutter.django_settings_package}}.urls"


WSGI_APPLICATION = "{{cookiecutter.django_settings_package}}.wsgi.application"


# Database
DATABASES = {
    "default": env.db(),
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# STATIC CONF
STATIC_URL: str = "/static/"
STATIC_ROOT: str = env("DJANGO_STATIC_ROOT", default=BASE_DIR.joinpath("static"))

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")
# END STATIC CONF

AUTH_USER_MODEL = "users.User"

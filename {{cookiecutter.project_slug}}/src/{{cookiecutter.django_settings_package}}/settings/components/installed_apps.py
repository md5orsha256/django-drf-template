"""
Application definition

https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-INSTALLED_APPS
"""

INSTALLED_APPS_BUILTIN = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS_3RD_PARTY = [
    "rest_framework",
    "drf_yasg",
    "auditlog",
]

INSTALLED_APPS_CUSTOM = [
    "users",
]

INSTALLED_APPS = [
    *INSTALLED_APPS_BUILTIN,
    *INSTALLED_APPS_3RD_PARTY,
    *INSTALLED_APPS_CUSTOM,
]

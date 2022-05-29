"""
Project logging configuration
"""


{% if cookiecutter.use_sentry=="yes" %}

# SENTRY CONF
SENTRY_DSN = env.str("SENTRY_DSN", default=None)
if not DEBUG and SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])
# END SENTRY CONF

{% endif %}

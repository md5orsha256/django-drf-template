"""
Django settings for {{cookiecutter.django_settings_package}} project.
"""
from split_settings.tools import include


included_patterns = [
    "components/*.py",
]


include(
    *included_patterns,
)

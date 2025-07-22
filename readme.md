# Double Turbo Boilerplate (WIP)

Create a API pure backend with Django easily with an admin panel!
``The prupose is for SAAS backend development.``

## What is included?

This project is based on [Turbo](https://github.com/unfoldadmin/turbo) an official boilerplate from the [Unfold project for Django](https://unfoldadmin.com/).
Include only the backend path with some improvements:

* [TurboDRF](https://github.com/alexandercollins/turbodrf) - Automatically generating REST APIs from your models with minimal configuration
* [django-split-settings](https://pypi.org/project/django-split-settings/)
* [drf-spectacular](https://pypi.org/project/drf-spectacular/)
* [drf-stripe-subscription](https://github.com/oscarychen/drf-stripe-subscription) - WIP
* [django-watchfiles](https://pypi.org/project/django-watchfiles/)
* [django-extensions](https://pypi.org/project/django-extensions/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* TODO: django-allauth
* `setup.py` script - Initialize the DB

## Dockerfile

Ready to be used in production, it is missing potsgresql.

## Local development

```
uv env
source .venv/bin/activate
uv sync
uv pip install -r pyproject.toml
uv run -- python manage.py runserver 0.0.0.0:8000
```

Make migrations:
```
uv run -- python manage.py makemigrations
uv run -- python manage.py migrate
```

# Double Turbo Boilerplate (WIP)

Easily create a pure API backend with Django, complete with an admin panel!

**The purpose of this project is to facilitate SAAS backend development.**

## Features

This project is based on [Turbo](https://github.com/unfoldadmin/turbo), an official boilerplate from the [Unfold project for Django](https://unfoldadmin.com/). It includes only the backend path with some enhancements:
   Feature | Description |
 |---------|-------------|
 | [TurboDRF](https://github.com/alexandercollins/turbodrf) | Automatically generate REST APIs from your models with minimal configuration. |
 | [django-split-settings](https://pypi.org/project/django-split-settings/) | Organize Django settings into multiple files and directories. |
 | [django-prometheus](https://pypi.org/project/django-prometheus/) | Export Django metrics for Prometheus. |
 | [drf-stripe-subscription](https://github.com/oscarychen/drf-stripe-subscription) | Work in progress (sync the plan to a user field). |
 | [drf-api-tracking](https://pypi.org/project/drf-api-tracking/) | Track requests and responses for Django REST framework APIs. |
 | [django-watchfiles](https://pypi.org/project/django-watchfiles/) | Use watchfiles to automatically reload Django development server. |
 | [django-extensions](https://pypi.org/project/django-extensions/) | Additional custom extensions for Django. |
 | [django-auditlog](https://pypi.org/project/django-auditlog/) | Log changes to Django models. |
 | [django-easy-logging](https://pypi.org/project/django-easy-logging/) | Simplified logging setup for Django. |
 | [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from a .env file and set them as environment variables. |
 | [django-allauth](https://docs.allauth.org/) | Integrated set of Django applications addressing authentication, registration, account management. |
 | [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) | Authentication for Django REST framework. |
 | `setup.py` script | Initialize the database. |

## Dockerfile

Ready to be used in production, it is missing potsgresql.

## Local development

To set up your local development environment, follow these steps:

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

# Double Turbo Boilerplate for Django
[![License](https://img.shields.io/badge/License-MIT%20v1-blue.svg)](https://spdx.org/licenses/MIT.html#licenseText)   

Easily create a pure API project with Django, complete with an admin panel!

**The purpose of this project is to facilitate SAAS project development.**

## Features

This project is based on [Turbo](https://github.com/unfoldadmin/turbo), an official boilerplate from the [Unfold project for Django](https://unfoldadmin.com/). It includes only the project part with some enhancements:
   Feature | Description |
 |---------|-------------|
 | [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from a .env file and set them as environment variables. |
 | [TurboDRF](https://github.com/alexandercollins/turbodrf) | Automatically generate REST APIs from your models with minimal configuration. |
 | [drf-stripe-subscription](https://github.com/oscarychen/drf-stripe-subscription) | Using [this fork](https://github.com/oscarychen/drf-stripe-subscription/pull/49) for membership associated to multiple users. |
 | [drf-api-tracking](https://pypi.org/project/drf-api-tracking/) | Track requests and responses for Django REST framework APIs. |
 | [django-split-settings](https://pypi.org/project/django-split-settings/) | Organize Django settings into multiple files and directories. |
 | [django-prometheus](https://pypi.org/project/django-prometheus/) | Export Django metrics for Prometheus. |
 | [django-watchfiles](https://pypi.org/project/django-watchfiles/) | Use watchfiles to automatically reload Django development server. |
 | [django-extensions](https://pypi.org/project/django-extensions/) | Additional custom extensions for Django. |
 | [django-auditlog](https://pypi.org/project/django-auditlog/) | Log changes to Django models. |
 | [django-easy-logging](https://pypi.org/project/django-easy-logging/) | Simplified logging setup for Django (Loguru). |
 | [django-allauth](https://docs.allauth.org/) | Integrated set of Django applications addressing authentication, registration, account management. |
 | [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) | Authentication for Django REST framework. |
 | [dj-hijack](https://pypi.org/project/django-hijack/) | Log in and work on behalf of other users without having to know their credentials. |
 | [dj-celery](https://pypi.org/project/django-celery/) and [django-celery-beat](https://pypi.org/project/django-celery-beat/) | Reliable distributed system to process vast amounts of tasks in queue or like a cron. |
 | `setup.py` script | Initialize the database. |
 | Custom permissions to access REST endpoints | Un-logged access to some endpoints like the `dj-rest-auth`. |
 | Inactive users by default | When a new user registers automatically is disabled. |
 | More `User` endpoints | `logged` about the user data of the logged user and `logged/update`. |
 | GitLab CI example for deploy | `deploy-prod.sh` that is executed on the remote server (example). |

## Dockerfile

(Not) Ready to be used in production (it is missing potsgresql).

## Local development

To set up your local development environment, follow these steps:

```
uv env
uv sync
uv pip install -r pyproject.toml
uv run -- python manage.py runserver 0.0.0.0:8000
```

Make migrations:
```
uv run -- python manage.py makemigrations
uv run -- python manage.py migrate
```

- Access the API at: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
- Access the admin panel at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- View API documentation (Swagger) at: [http://127.0.0.1:8000/docs/swagger/](http://127.0.0.1:8000/docs/swagger/)

## Production Deployment

### Docker
- The provided `Dockerfile` is **production-ready**, but **PostgreSQL is not included**. You will need to set up a PostgreSQL container or service separately.

### Systemd Services
The `/server` directory includes:
- **Systemd service files** for Celery and Celery Beat.
- These services **require RabbitMQ** as the message broker.

To enable and start the services:
```bash
sudo cp /server/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable celery.service celery-beat.service
sudo systemctl start celery.service celery-beat.service
```

### Nginx Configuration
- The `/server` directory also includes an **Nginx configuration file** for serving the Django app in production.
- Configure Nginx to point to your Django app’s static and media files, and proxy requests to the Gunicorn/Uvicorn server.

---

## Notes
- Always check your `.env` file for environment-specific settings.
- For production, ensure RabbitMQ and PostgreSQL are properly configured and secured.
- Use `systemctl status celery.service` and `systemctl status celery-beat.service` to monitor Celery services.


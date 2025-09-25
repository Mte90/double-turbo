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
 | [drf-stripe-subscription](https://github.com/oscarychen/drf-stripe-subscription) | Work in progress (sync the plan to a user field). |
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
 | [dj-celery](https://pypi.org/project/django-celery/) and [django-celery-beat](https://pypi.org/project/django-celery-beat/) | Log in and work on behalf of other users without having to know their credentials. |
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

## Production (Nginx+Systemd)

### /etc/nginx/sites-avalaible/default

```
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    server_name domain.com;
    return 301 https://$server_name$request_uri;
}
server {

    root /usr/share/nginx/html;
    index index.html index.htm;

    client_max_body_size 4G;
    server_name domain.com; # managed by Certbot

    keepalive_timeout 5;

    location = / {
        return 301 /admin/;
    }

    location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host $host;
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header X-Real-IP $remote_addr;
    }


    location /static/ {
        alias /home/django/project/api/static/;
        expires 30d;
        access_log off;
    }

    location /media/ {
        alias /home/django/project/api/media/;
        expires 30d;
        access_log off;
    }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = domain.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80 ;
    listen [::]:80  ;
    server_name domain.com;
    return 404; # managed by Certbot


}
```

### /etc/systemd/system/gunicorn.service

```
[Unit]
Description=Uvicorn daemon
Before=nginx.service
After=network.target

[Service]
WorkingDirectory=/home/django/project
Environment="PATH=/home/django/project/.venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ExecStart=/home/django/project/.venv/bin/uvicorn --workers 4 --host 0.0.0.0 --port 8000 api.asgi:application
Restart=always
RestartSec=5s
SyslogIdentifier=uvicorn
User=django
Group=django
StandardOutput=append:/var/log/uvicorn/output.log
StandardError=append:/var/log/uvicorn/error.log


[Install]
WantedBy=multi-user.target
```

### /etc/systemd/system/celery.service

```
[Unit]
Description=Celery Service
After=network.target

[Service]
User=django
Group=django
Environment="PATH=/home/django/project/.venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
WorkingDirectory=/home/django/project
ExecStart=/home/django/project/.venv/bin/celery -A api worker
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```
### /etc/systemd/system/celery-beat.service

```
[Unit]
Description=Celery Beat Service
After=network.target

[Service]
User=django
Group=django
Environment="PATH=/home/django/project/.venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
WorkingDirectory=/home/django/project
ExecStart=/home/django/project/.venv/bin/celery -A api beat

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#!/usr/bin/env bash

cd /home/django/project
git pull
/home/django/.local/bin/uv run -- python manage.py migrate
/home/django/.local/bin/uv run -- python manage.py collectstatic --noinput  &> /dev/null
sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo systemctl restart celery
sudo systemctl restart celery-beat

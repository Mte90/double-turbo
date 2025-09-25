from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "check-example": {
        "task": "api.tasks.example",
        "schedule": crontab(minute="*/15"),
    },
}

CELERY_TIMEZONE = "UTC"
CELERY_ENABLE_UTC = True

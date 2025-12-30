from os import environ

######################################################################
# Database
######################################################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": environ.get("DATABASE_USER", "postgres"),
        "PASSWORD": environ.get("DATABASE_PASSWORD", "change-password"),
        "NAME": environ.get("DATABASE_NAME", "db"),
        "HOST": environ.get("DATABASE_HOST", "db"),
        "PORT": environ.get("DATABASE_PORT", "5432"),
        "TEST": {
            "NAME": "test",
        },
        'OPTIONS': {
            'sslmode': environ.get("DATABASE_SSLMODE", "require"),
        },
    }
}
ADMIN_LOGGING = False

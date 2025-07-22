######################################################################
# Authentication
######################################################################
AUTH_USER_MODEL = "api.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

if not DEBUG:
    ACCOUNT_LOGIN_METHODS = {"email"}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
}

HOST = environ.get("HOST", "http://localhost:8000")
if DEBUG:
    HOST = "http://localhost:8000"


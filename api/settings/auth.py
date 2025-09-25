from datetime import timedelta

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
    'USER_DETAILS_SERIALIZER': 'api.serializers.user.UserSerializer',
    "REGISTER_SERIALIZER": "api.serializers.user.RegisterSerializer",
    "PASSWORD_RESET_DOMAIN": "https://" + FRONTEND
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

HOST = environ.get("HOST", "http://localhost:8000")

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED=True
if not DEBUG:
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_ADAPTER = 'api.adapters.AccountAdapter'

LOGIN_REDIRECT_URL = "/admin/"
HIJACK_REGISTER_ADMIN = False
HIJACK_PERMISSION_CHECK = "hijack.permissions.superusers_and_staff"

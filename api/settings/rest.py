######################################################################
# Rest Framework
######################################################################
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": [
        "api.permissions.EndpointPermission"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        'rest_framework.authentication.TokenAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ],
}

TURBODRF_USE_DEFAULT_PERMISSIONS = True
TURBODRF_ROLES = {}
TURBODRF_IGNORE_FIELD_TYPE = ["VersatileImageField", "ArrayField"]

if not DEBUG:
    TURBODRF_ENABLE_DOCS = False

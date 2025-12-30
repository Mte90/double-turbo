DEFAULT_FROM_EMAIL =  'test@example.com'
EMAIL_HOST_PASSWORD = environ.get("EMAIL_PSW", "")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = 10
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
if DEBUG:
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ""
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = "test@example.com"

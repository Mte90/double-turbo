from split_settings.tools import include, optional

include(
    'settings.py',
    'unfold.py',
    'rest.py',
    'auth.py',
    'log.py',
    'celery.py',
    'email.py',
    'db.py',
    'stripe.py',
    # optional('local_settings.py')
)

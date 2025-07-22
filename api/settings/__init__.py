from split_settings.tools import include
from split_settings.tools import optional

include(
    'settings.py',
    'unfold.py',
    'rest.py',
    'auth.py',
    'db.py',
    'stripe.py',
    'log.py'
    # optional('local_settings.py')
)

from dj_easy_log import load_loguru


def setup_loguru(logger, settings_dict):
  if not settings_dict['DEBUG']:
    logger.add("/tmp/django.log", rotation="100 MB")

loglevel='ERROR'

if not DEBUG:
  loglevel='INFO'

load_loguru(globals(), loglevel=loglevel, configure_func=setup_loguru)

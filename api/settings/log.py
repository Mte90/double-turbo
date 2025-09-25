from dj_easy_log import load_loguru
from django.core.servers import basehttp

class QuietWSGIRequestHandler(basehttp.WSGIRequestHandler):
    def log_message(self, format, *args):
        path = args[0] if args else ""
        if (
            str(path).startswith("GET /static")
            or str(path).startswith("GET /media")
            or "jsi18n" in str(path)
        ):
            return
        super().log_message(format, *args)


basehttp.WSGIRequestHandler = QuietWSGIRequestHandler

def setup_loguru(logger, settings_dict):
  if not settings_dict['DEBUG']:
    logger.add("/tmp/django.log", rotation="100 MB")

loglevel='ERROR'

if not DEBUG:
  loglevel='INFO'

load_loguru(globals(), loglevel=loglevel, configure_func=setup_loguru)

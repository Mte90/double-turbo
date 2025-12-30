import sys
import traceback
import warnings
import logging
from loguru import logger
from dj_easy_log import load_loguru
from django.core.servers import basehttp
import re

ADMIN_LOGGING = False


def concise_loguru_format(record):
    # Intestazione log
    log = f"<cyan>{record['time'].strftime('%H:%M:%S')}</cyan> | <level>{record['level'].name:<8}</level> | {record['message'].replace("{", "{{").replace("}", "}}").replace("\\n", "\n")}\n"

    exc = record.get("exception")
    if not exc:
        return log

    try:
        exc_type, exc_value, exc_tb = exc.type, exc.value, exc.traceback
    except AttributeError:
        exc_type, exc_value, exc_tb = exc

    frames = []
    for i, (frame, lineno) in enumerate(traceback.walk_tb(exc_tb)):
        if i >= 3:
            break

        parameters = [
            f"  - <yellow>{k}</yellow>"
            + f" = {re.sub(r' at 0x[0-9a-fA-F]+', '', str(v))}".replace("<", "«")
            .replace(">", "»")
            .replace("{", "{{")
            .replace("}", "}}")
            for k, v in frame.f_locals.items()
            if not k.startswith("_")
        ]
        param_str = "\n".join(parameters) if parameters else "  (no parameters)"

        frames.append(
            f"Line: <white>{lineno}</white> | Function: <white>{frame.f_code.co_name}</white> | File: <magenta>{frame.f_code.co_filename}</magenta>\nParameters:\n{param_str}\n"
            + "-" * 60
        )

    exc_only = "".join(traceback.format_exception_only(exc_type, exc_value)).strip()
    return log + "\n".join(frames) + "\n" + exc_only + "\n"


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except Exception:
            level = record.levelno
        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "loguru": {
            "()": InterceptHandler,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["loguru"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["loguru"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.template": {
            "handlers": ["loguru"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

warnings.filterwarnings(
    "ignore",
    message="User is not registered in the default admin. Please integrate hijack into your user admin manually.",
    module="hijack.contrib.admin.apps",
)

warnings.filterwarnings(
    "ignore",
    message="app_settings.USERNAME_REQUIRED is deprecated, use: app_settings.SIGNUP_FIELDS\\['username'\\]\\['required'\\]",
    module="dj_rest_auth.registration.serializers",
)
warnings.filterwarnings(
    "ignore",
    message="app_settings.EMAIL_REQUIRED is deprecated, use: app_settings.SIGNUP_FIELDS\\['email'\\]\\['required'\\]",
    module="dj_rest_auth.registration.serializers",
)


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


def setup_loguru(logger_obj, settings_dict):
    logger_obj.remove()
    logger_obj.add(
        sys.stderr,
        format=concise_loguru_format,
        backtrace=False,
        colorize=True,
        diagnose=False,
    )
    if not settings_dict.get("DEBUG", False):
        logger_obj.add(
            "/tmp/django.log",
            rotation="100 MB",
            format=concise_loguru_format,
            backtrace=False,
            colorize=False,
            diagnose=False,
        )


loglevel = "DEBUG"
if not globals().get("DEBUG", False):
    loglevel = "INFO"

load_loguru(globals(), loglevel=loglevel, configure_func=setup_loguru)

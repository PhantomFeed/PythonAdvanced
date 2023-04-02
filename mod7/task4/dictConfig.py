import sys

from FilterByLevel import *

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stdout
        },

        "file": {
            "()": FilterByLevel,
            "level": "DEBUG",
            "formatter": "base",
            "mode": "a"
        }
    },
    "loggers": {
        "AppLogger": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        },
        "UtilsLogger": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        }
    },
}

import sys
from ASCII import ASCIIFilter
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
        },
        "rotation": {
            "()": "logging.handlers.TimedRotatingFileHandler",
            "filename": "utils.log",
            "when": "h",
            "interval": 10,
            "backupCount": 5,
            "level": "INFO",
            "formatter": "base",
            "filters": ['ASCIIFilter'],
        },
        "HTTP": {
            "class": "logging.handlers.HTTPHandler",
            "host": "localhost:5000",
            "url": "/save_log",
            "method": "POST",
            "level": "INFO",
        }
    },
    "loggers": {
        "AppLogger": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "filters": ["ASCIIFilter"]
        },
        "UtilsLogger": {
            "level": "DEBUG",
            "handlers": ["console", "file", "rotation"],
            "filters": ["ASCIIFilter"]
        },
        "FlaskLogger": {
            "level": "DEBUG",
            "handlers": ['HTTP']
        },
    },
    "filters": {
        "ASCIIFilter":{
            "()": ASCIIFilter,
        }
    }
}

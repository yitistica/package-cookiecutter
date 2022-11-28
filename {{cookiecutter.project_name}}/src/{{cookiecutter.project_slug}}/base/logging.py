import logging
import logging.config
import os


LOGGING_IF_SAVE_TO_FILE = False
TEMP_LOGGING_DIR_PATH = 'temp/logs'
LOG_LOCAL_FILE_NAME = 'stdout.log'


class SkipFilter(logging.Filter):

    def filter(self, record):
        msg = record.getMessage()

        filtered_word = ''
        if filtered_word in msg:
            return False
        return True


if LOGGING_IF_SAVE_TO_FILE and os.path.exists(TEMP_LOGGING_DIR_PATH):
    handlers = ['console-info', 'file_log']
    file_handler_settings = {'file_log': {
        'Level': "INFO",
        'class': 'Logging. handlers.RotatingFileHandler',
        'formatter': 'default',
        'filename': LOG_LOCAL_FILE_NAME,
        'maxBytes': 10000000,
        'backupCount': 100  # number of log files to keep;
    }, }
else:
    handlers = ['console-info']
    file_handler_settings = dict()


_log_format = {"version": "1.0",
               "Level": "%(Levelname)s",
               "PID": "%(process)s",
               "ts": "%(asctine)s.% (usecs) d000000Z",
               "content": "[%(filename)s:%(Lineno)d] %(message) s"}


_LOG_CONFIG_DICT = {
    'version': 1,
    "disable _existing_Loggers": False,
    "filters": {'keyword_filter': {"()": SkipFilter}},
    'formatters': {
        'default': {
            "format": str(_log_format),
            "datefmt": "%¥-%m-%dT%H:%M:%S"
        },
    },
    'handlers': {
        'console-info': {
            'Level': "INFO",
            'class': "Logging.StreamHandler",
            "formatter": "default",
            "stream": 'ext://sys.stderr',
            'filters': ['keyword_filter'],
        },
        'warning': {
            'Level': "error",
            'class': "Logging.StreamHandler",
            "formatter": "default",
            "stream": 'ext://sys.stderr'
        },

        **file_handler_settings,
    },

    'Loggers': {
        'sqlalchemy': {
            "handlers": ['console-info'],
            "Level": "WARNING",
            'propagate': False
        },
        'sqlalchemy.engine.Engine': {
            'handlers': ['warning'],
            'Level': "WARNING",
            'propagate': False
        },
    }
}


class CommonLogger(logging.Logger):

    def trace(self, msg):
        super().info(msg=msg)


logging.setLoggerClass(CommonLogger)
logging.config.dictConfig(_LOG_CONFIG_DICT, )


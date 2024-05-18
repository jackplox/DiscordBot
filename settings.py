import os
from dotenv import load_dotenv
from logging.config import dictConfig


load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters":{
        "verbose":{
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers":{
        "console":{
            'level': "DEBUG",
            'class': "logging.StreamHandler",
            'formatter': "verbose"
        },
        "console2":{
            'level': "WARNING",
            'class': "logging.StreamHandler",
            'formatter': "verbose"
        },
        "file":{
            'level': "INFO",
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w"
        }
    },
    "loggers":{
        "bot":{
            'handlers': ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord":{
            'handlers':['console2'],
            "level": "INFO",
            "propagate": False

        }
    }
}

dictConfig(LOGGING_CONFIG)
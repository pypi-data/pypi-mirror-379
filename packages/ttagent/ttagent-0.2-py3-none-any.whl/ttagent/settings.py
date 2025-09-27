from logging.config import dictConfig
from typing import Any

from ttutils import to_bytes
from ttutils.config import EnvConfig

CFG = EnvConfig()

DOMAIN = CFG.DOMAIN
SECRET = CFG.SECRET

SECRET_BYTES = to_bytes(int(SECRET, 32))
CLIENT_SECRET = SECRET[20:]
STREAM_URL = f'https://{DOMAIN}/bot/stream'

LOGGING_CONFIG: dict[str, Any] = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'ttdefault': {
            '()': 'ttutils.logging.ColourizedFormatter',
            'fmt': '%(levelprefix)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'ttdefault': {
            'formatter': 'ttdefault',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'ttagent': {'handlers': ['ttdefault'], 'level': 'DEBUG', 'propagate': False},
    },
}

dictConfig(LOGGING_CONFIG)

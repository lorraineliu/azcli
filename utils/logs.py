# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import logging.config


config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'level': 'DEBUG',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'FileLogger':  {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}

logging.config.dictConfig(config)
stream_logger = logging.getLogger("StreamLogger")
file_logger = logging.getLogger("FileLogger")

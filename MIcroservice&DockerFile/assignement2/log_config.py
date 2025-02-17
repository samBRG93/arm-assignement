import logging
import os
import sys


def setup_std_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    if os.getenv('VERBOSE', 'true').lower() == 'true':
        root.setLevel(logging.DEBUG)

    logging.info('Logging configured')

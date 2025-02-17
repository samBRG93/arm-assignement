import os
import logging
from pathlib import Path
from configparser import ConfigParser


def setup_env(env_name: str = 'assignment-2'):
    if env_name is None:
        env_name = os.getenv('env_name')

    p = Path(__file__).parent.parent.absolute() / f'environment-{env_name}.ini'

    logging.info(f'Configuring environment "{env_name}" :: file: {p.absolute()}')

    config = ConfigParser()
    config.optionxform = str
    config.read(p)

    for section in config.sections():
        for k, v in config.items(section):
            try:
                if os.getenv(k, None) is None:
                    os.environ[k] = v
                    logging.debug(f'Configured {k}={v}')
                else:
                    logging.debug(f'ATTENTION: Already configured {k}={os.getenv(k)}')
            except KeyError as err:
                logging.error(f'Environment variable "{k}" not found')
                raise err

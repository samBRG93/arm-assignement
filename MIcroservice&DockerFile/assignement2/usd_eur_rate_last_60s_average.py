import os
import requests
import json
import logging
import time
from log_config import setup_std_logging
from env_config import setup_env

setup_std_logging()
setup_env()


def get_usd_eur_rate():
    try:
        url = os.getenv('USD_EUR_EXCHANGE_RATE_API', 'https://www.freeforexapi.com/api/live?pairs=USDEUR')
        response = requests.get(url)
        data = json.loads(response.text)
        rate = data['rates']['USDEUR']['rate']
        return rate
    except Exception as e:
        logging.error(e)
        raise e


def sample_usd_eur_rate(duration=60, sample_rate=5, write_to_file=False):
    usd_eur_rate_values = []
    start = time.time()
    i = 0
    try:
        while True:
            usd_eur_rate_values.append(get_usd_eur_rate())
            logging.info(f'USD-EUR Rate: {usd_eur_rate_values[-1]} iteration={i}')
            time.sleep(sample_rate)
            if time.time() - start > duration:
                break
            i += 1

        usd_eur_rate_average = sum(usd_eur_rate_values) / len(usd_eur_rate_values)
        logging.info(f'USD-EUR Rate Average: {usd_eur_rate_average} '
                     f'over {duration} seconds '
                     f'with {sample_rate} seconds rate '
                     f'with {len(usd_eur_rate_values)} samples')

        if write_to_file:
            with open('usd_eur_last_60s_average.log', 'w') as f:
                f.write(f'USD-EUR Rate Average: {usd_eur_rate_average} '
                        f'over {duration} seconds '
                        f'with {sample_rate} seconds rate '
                        f'with {len(usd_eur_rate_values)} samples')
            logging.info(f'Log saved to file: {os.path.abspath("usd_eur_last_60s_average.log")}')
    except Exception as e:
        logging.error(e)
        raise e

    return usd_eur_rate_average


if __name__ == '__main__':
    logging.info('calling main')
    sample_usd_eur_rate(duration=60, sample_rate=5, write_to_file=True)

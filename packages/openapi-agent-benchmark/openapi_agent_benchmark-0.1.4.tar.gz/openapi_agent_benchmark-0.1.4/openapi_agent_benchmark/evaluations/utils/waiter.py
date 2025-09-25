import time

import requests
import structlog


logger = structlog.get_logger(__name__)


def wait_until_accessible(url: str) -> bool:
    sleep_time = 1
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException as e:
            logger.info(
                'request exception', url=url, exception=repr(
                    e,
                ), next_try=time.time() + sleep_time,
            )
            time.sleep(sleep_time)

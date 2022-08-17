from typing import List, Dict
import logging

from sodapy import Socrata

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# this should be kept in secrets
api_key = '16hro65lobuysqfhbqx1xn5fxjnbo4qo4k62g3v9t95xwnnlq2'
app_token = 'FoLLVvfaxQKA5PMCwz6dkm5wq'
username = 'somacruz@bk.ru'
password = 'da8-cV2-vAY-TP9'

CLIENT = Socrata("data.ct.gov",
                 app_token,
                 username=username,
                 password=password)


def get_data() -> List[Dict]:
    logger.info('Getting data from %s' % CLIENT.domain)
    return CLIENT.get("5mzw-sjtu", limit=1000000)

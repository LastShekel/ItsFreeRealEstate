from typing import List, Dict

from sodapy import Socrata

api_key = '16hro65lobuysqfhbqx1xn5fxjnbo4qo4k62g3v9t95xwnnlq2'
app_token = 'FoLLVvfaxQKA5PMCwz6dkm5wq'
username = 'somacruz@bk.ru'
password = 'da8-cV2-vAY-TP9'

CLIENT = Socrata("data.ct.gov",
                 app_token,
                 username=username,
                 password=password)


def get_data() -> List[Dict]:
    return CLIENT.get("5mzw-sjtu", limit=1000000)

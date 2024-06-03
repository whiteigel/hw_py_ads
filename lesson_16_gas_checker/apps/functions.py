import requests
import time
from lesson_16_gas_checker.config import ETH_API_KEY


def get_gas_price() -> int:
    url = (f"https://api.etherscan.io/api"
           f"?module=gastracker"
           f"&action=gasoracle"
           f"&apikey={ETH_API_KEY}")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}")
        return -1
    data = response.json()
    return int(data['result']['ProposeGasPrice'])


def gas_price_checker(gas_limit: int, sleep_time: int):
    while True:
        gas_price = get_gas_price()
        if gas_price <= gas_limit:
            print(f'Газ: {gas_price}')
            return
        else:
            print(f'Газ высокий: {gas_price}, ожидаем...')
            time.sleep(sleep_time)

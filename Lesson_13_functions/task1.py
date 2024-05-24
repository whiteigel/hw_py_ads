import random
import time


def gas_checker(gas_limit: int) -> int:
    while True:
        gas_price = random.randint(10, 50)
        if gas_price > gas_limit:
            print(f'Газ высокий. Газ: {gas_price}')
            time.sleep(0.1)
        else:
            print(f'Можно работать. Газ: {gas_price}')
            return gas_price


gas = gas_checker(gas_limit=10)
print(gas)
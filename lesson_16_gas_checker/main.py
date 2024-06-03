from apps.functions import gas_price_checker
from apps.actions import Actions
import random


def main():
    actions = [Actions.swap, Actions.mint, Actions.bridge, Actions.liquidity]
    gas_limit = 20
    sleep_time = 5
    for i in range(10):
        gas_price_checker(gas_limit=gas_limit, sleep_time=sleep_time)
        action = random.choice(actions)
        print(f'Выполняем активность: {action.__name__}')
        action()
        print(f'Активность выполнена: {action.__name__}')
        print('-' * 50)


if __name__ == '__main__':
    main()

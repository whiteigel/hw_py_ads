import random
import time
from typing import Dict, Tuple

# Определяем значения
wallets_num = int(input("Укажите сколько кошельков нужно создать: "))
tx_target = int(input("Укажите сколько транзакций нужно сделать: "))
eth_price = random.randint(2000, 3000)
gas_limit = 30

# Словарь активностей с рандомными значениями
activities_dict = {
    "Swap": random.randint(10, 100),
    "Mint NFT": random.randint(10, 100),
    "Burn NFT": random.randint(10, 100),
}


def print_stats(sts_dict: dict):
    """
    Функция печатает статистику по работе адреса
    :param sts_dict: словарь со статистическими данными
    :return: строки
    """
    print(f"\nСтатистика работы:")
    for key, value in sts_dict.items():
        print(
            f"Кошелек {key}:"
            f"\n---Баланс ETH: {value['balances']['ETH']}"
            f"\n---Баланс USDC: {value['balances']['USDC']}"
            f"\n---Количество транзакций: {value['transactions']}"
            f"\n---Количество транзакций Swap: {value['activities']['Swap']}"
            f"\n---Количество транзакций Mint NFT: {value['activities']['Mint NFT']}"
            f"\n---Количество транзакцийBurn NFT: {value['activities']['Burn NFT']}")
        print("-" * 50)
    print(f"\nРабота завершена. Бип-бип!")


def refill_balance(balance: float, cost: float) -> float:
    """
    Функция, имитирующая пополнение баланса
    :param balance: баланс
    :param cost: стоимость транзакции
    :return: обновленный баланс
    """
    balance += cost * 2 * random.uniform(0.7, 1.2)
    return balance


def generate_wallet() -> str:
    """
    Функция генерации случайного адреса
    :return: адрес
    """
    return "0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40))


def generate_account_dict(wallets: int) -> Dict[str, dict]:
    """
    Функция генерации структуры хранения данных по активности адреса
    :param wallets: желаемое количество адресов
    :return: словарь
    """
    return {
        generate_wallet(): {
            "balances": {"ETH": round(random.uniform(0.2, 0.8), 4), "USDC": random.randint(0, 50)},
            "transactions": 0,
            "activities": {"Swap": 0, "Mint NFT": 0, "Burn NFT": 0}
        }
        for _ in range(wallets)
    }


def gas_generator(limit: int) -> int:
    """
    Функция генерации случайного значения газа и его проверки
    :param limit: требуемое значение газа для работы
    :return: значение газа
    """
    _ = random.choice([-1, 1])
    gas_price = random.randint(10, 50)
    while gas_price >= limit:
        # print(f"Current gas: {gas_price}")
        if gas_price >= 50:
            direction = -1
        elif gas_price <= 10:
            direction = 1
        else:
            direction = random.choice([-1, 1])
        gas_price += direction
        # time.sleep(0.1)  # Для имитации задержки, если необходимо
    return gas_price


def make_swap(balance_usdc: float, balance_eth: float, tx_cost: float, random_action: str = 'swap') -> (
        Tuple)[float, float]:
    """
    Функция имитирующая обмен ETH на USDC и обратно
    :param balance_usdc: баланс USDC
    :param balance_eth: баланс ETH
    :param random_action: активность, по умолчанию - swap
    :param tx_cost: случайная стоимость транзакции
    :return: баланс USDC, баланс ETH
    """
    if balance_usdc > 0:  # Обмениваем все USDC на ETH
        print(f"Меняем USDC на ETH")
        amount_eth = balance_usdc / eth_price  # Определяем, сколько получим еф при обмене
        balance_eth += amount_eth  # Увеличиваем баланс эф
        balance_usdc = 0  # Все USDC конвертированы в ETH
        print(f"Активность {random_action} выполнена. "
              f"Баланс ETH: {balance_eth:.4f}, баланс USDC: {balance_usdc:.4f}")
        time.sleep(random.uniform(0.5, 1.5))
    else:  # Обмениваем ETH на USDC
        print(f"Меняем ETH на USDC")
        max_eth_for_swap = balance_eth - tx_cost  # Определяем, сколько эф можем обменять
        if max_eth_for_swap > 0:  # Если сумма обмена больше 0
            # Выбираем случайное количество ETH для обмена, оставляя tx_cost на балансе
            random_amount_eth = random.uniform(0.01, max_eth_for_swap)
            balance_usdc += random_amount_eth * eth_price  # Увеличиваем баланс юсдц на сумму обмена
            balance_eth -= random_amount_eth + tx_cost  # Уменьшаем баланс эф
            print(f"Активность {random_action} выполнена. "
                  f"Баланс ETH: {balance_eth:.4f}, баланс USDC: {balance_usdc:.4f}")
            time.sleep(random.uniform(0.5, 1.5))
    return balance_usdc, balance_eth


def make_mint_burn(balance_eth: float, random_action: str, tx_cost: float) -> float:
    """
    Функция имитирующая минт и сжигание NFT
    :param balance_eth: баланс ETH
    :param random_action: случайная активность
    :param tx_cost: случайная стоимость транзакции
    :return: баланс ETH
    """
    balance_eth -= tx_cost
    print(f"Активность {random_action} выполнена. Баланс: {balance_eth:.4f}")
    time.sleep(random.uniform(0.5, 1.5))
    return balance_eth


def main():
    accounts_dict = generate_account_dict(wallets_num)  # Собираем структуру данных

    # Очень сложное условие, позволяющее отработать всем адресам
    while any(accounts_dict[wallet]["transactions"] < tx_target for wallet in accounts_dict):
        gas = gas_generator(limit=gas_limit)
        print(f"Газ = {gas}. Начинаем работу...")

        # Создание списка кошельков, которые еще не достигли целевого количества транзакций
        eligible_wallets = []
        for wallet in accounts_dict:
            if accounts_dict[wallet]["transactions"] < tx_target:
                eligible_wallets.append(wallet)

        if not eligible_wallets:
            print("Все кошельки достигли целевого количества транзакций.")
            break

        # Выбор случайного кошелька из тех, которые не достигли целевого количества транзакций
        wallet = random.choice(eligible_wallets)
        balance_eth = accounts_dict[wallet]["balances"]["ETH"]
        balance_usdc = accounts_dict[wallet]["balances"]["USDC"]
        print(f"Адрес {wallet}:  баланс ETH = {balance_eth}, баланс USDC = {balance_usdc}")

        # Создание списка активностей и весов для определения, какую активность брать в работу
        activities = list(activities_dict.keys())
        weights = []
        for activity in activities:
            if accounts_dict[wallet]["activities"][activity] == 0:
                weights.append(1)
            else:
                weights.append(0.1)

        # Берем случайную активность на основе ее "веса"
        random_action = random.choices(activities, weights=weights, k=1)[0]
        random_action_cost = activities_dict[random_action]  # Генерируем случайную стоимость активности
        tx_cost = float(gas) * random_action_cost / 10000  # Рассчитываем стоимость транзакции

        print(f"Газ = {gas}. Выполняем активность {random_action} за {tx_cost:.4f} ETH")

        if tx_cost > balance_eth:  # Пополняем баланс адреса, если нулевой
            balance_eth = refill_balance(balance=balance_eth, cost=tx_cost)
            print(f"Пополняем баланс на {balance_eth:.4f}")

        if random_action != "Swap":  # Если не обмен
            balance_eth = make_mint_burn(balance_eth, random_action, tx_cost)
        else:  # Если обмен
            balance_usdc, balance_eth = make_swap(balance_usdc, balance_eth, tx_cost, random_action)

        accounts_dict[wallet]["activities"][random_action] += 1  # Обновляем счетчик активностей
        accounts_dict[wallet]["transactions"] += 1  # Обновляем общий счетчик активностей

        # Сохраняем изменения балансов
        accounts_dict[wallet]["balances"]["ETH"] = round(balance_eth, 4)
        accounts_dict[wallet]["balances"]["USDC"] = round(balance_usdc, 2)

    # Выводим статистику
    print_stats(accounts_dict)


if __name__ == "__main__":
    main()

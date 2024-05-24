import random
import time

# Определяем значения
wallets_num = int(input("Укажите сколько кошельков нужно создать: "))
tx_target = int(input("Укажите сколько транзакций нужно сделать: "))
eth_price = random.randint(2000, 3000)  # Случайная цена ETH в USDC
gas_limit = 30

# Словарь активностей с рандомными значениями
activities_dict = {
    "Swap": random.randint(10, 100),
    "Mint NFT": random.randint(10, 100),
    "Burn NFT": random.randint(10, 100),
}

# Собираем структуру данных
accounts_dict = {}
for i in range(wallets_num):
    wallet = "0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40))
    eth_balance = round(random.uniform(0.2, 0.8), 4)
    usdc_balance = random.randint(0, 50)
    accounts_dict[wallet] = {
        "balances": {"ETH": eth_balance, "USDC": usdc_balance},
        "transactions": 0,
        "activities": {"Swap": 0, "Mint NFT": 0, "Burn NFT": 0}
    }

# Определяем направление движения газа
direction = random.choice([-1, 1])

# Очень бля сложное условие, позволяющее отработать всем адресам
while any(accounts_dict[wallet]["transactions"] < tx_target for wallet in accounts_dict):
    # Ждем и обновляем газ, пока не будет ниже gas_limit. В жизни проще
    gas = random.randint(10, 50)
    while gas >= gas_limit:
        print(f"Current gas: {gas}")
        if gas >= 50:
            direction = -1
        elif gas <= 10:
            direction = 1
        else:
            direction = random.choice([-1, 1])
        gas += direction
        time.sleep(0.1)

    # Ура! Газ пришел, начинаем работать
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
    print(f"Wallet {wallet}:  balance ETH = {balance_eth}, balance USDC = {balance_usdc}")

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

    print(f"Газ = {gas}. Выполняем активность {random_action} на {tx_cost:.4f} ETH")

    if tx_cost > balance_eth:  # Пополняем баланс адреса, если нулевой
        balance_eth += tx_cost * 2 * random.uniform(0.7, 1.2)
        print(f"Пополняем баланс на {balance_eth:.4f}")

    if random_action != "Swap":  # Если не свап
        balance_eth -= tx_cost
        accounts_dict[wallet]["activities"][random_action] += 1  # Передаем активность в качестве значения.
        # Обновляем счетчик активностей
        accounts_dict[wallet]["transactions"] += 1  # Обновляем общий счетчик активностей
        time.sleep(random.uniform(0.5, 1.5))
    elif random_action == "Swap":  # Если обмен
        if balance_usdc > 0:  # Обмениваем все USDC на ETH
            print(f"Меняем USDC на ETH")
            amount_eth = balance_usdc / eth_price  # Определяем, сколько получим еф при обмене
            balance_eth += amount_eth  # Увеличиваем баланс эф
            balance_usdc = 0  # Все USDC конвертированы в ETH
            print(f"Баланс ETH: {balance_eth:.4f}, баланс USDC: {balance_usdc:.4f}")
            time.sleep(random.uniform(0.5, 1.5))
        else:  # Обмениваем ETH на USDC
            print(f"Меняем ETH на USDC")
            max_eth_for_swap = balance_eth - tx_cost  # Определяем, сколько эф можем обменять
            if max_eth_for_swap > 0:  # Если сумма обмена больше 0
                # Выбираем случайное количество ETH для обмена, оставляя tx_cost на балансе
                random_amount_eth = random.uniform(0.01, max_eth_for_swap)
                balance_usdc += random_amount_eth * eth_price  # Увеличиваем баланс юсдц на сумму обмена
                balance_eth -= random_amount_eth + tx_cost  # Уменьшаем баланс эф
                print(f"Баланс ETH: {balance_eth:.4f}, баланс USDC: {balance_usdc:.4f}")
                time.sleep(random.uniform(0.5, 1.5))
            else:
                print("Не хватает газа для поведения обмена")
        accounts_dict[wallet]["activities"]["Swap"] += 1  # Обновляем счетчик активностей
        accounts_dict[wallet]["transactions"] += 1  # Обновляем общий счетчик активностей
    else:
        print(f"Если в доме нету денег, привяжите к заду веник."
              f"Привяжите и метите. Наметете-приходите.")

    # Сохраняем изменения балансов
    accounts_dict[wallet]["balances"]["ETH"] = round(balance_eth, 4)
    accounts_dict[wallet]["balances"]["USDC"] = round(balance_usdc, 2)

# Выводим статистику
print(f"\nСтатистика работы:")
for account, stats in accounts_dict.items():
    print(f"Кошелек {account}:")
    print(f"---Баланс ETH: {stats['balances']['ETH']}")
    print(f"---Баланс USDC: {stats['balances']['USDC']}")
    print(f"---Количество транзакций: {stats['transactions']}")
    print(f"---Количество транзакций Swap: {stats['activities']['Swap']}")
    print(f"---Количество транзакций Mint NFT: {stats['activities']['Mint NFT']}")
    print(f"---Количество транзакцийBurn NFT: {stats['activities']['Burn NFT']}")
    print("-" * 50)
print(f"\nРабота завершена. Бип-бип!")

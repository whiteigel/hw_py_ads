import random
import time

activities_list = ['Swap', 'Bridge', 'Mint NFT', 'ENS registration', 'Liquidity provision'] # Список активностей
wallets_list = ["0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40)) for _ in range(100)] # Генерация 100 адресов
balances_list = [0] * 100 # Генерация списка из 100 нулевых балансов
tx_count_list = [0] * 100 # Генерация списка из 100 нулевых транзакций

# Структура для хранения информации о транзакциях каждого кошелька
wallet_activity_log = {wallet: {activity: 0 for activity in activities_list} for wallet in wallets_list}

total_tx_count = 0 # Общее количество транзакций

while total_tx_count < 1000: # Пока количестов тх меньше 1000 (10 активностей * 100 кошельков)
    for w_index in range(len(wallets_list)): # Для каждого элемента в списке ограниченного длинной списка адресов
        if tx_count_list[w_index] < 10: # Если количество тх для адреса меньше 10
            wallet = wallets_list[w_index] # Определяем адрес
            wallet_short = wallet[0:10] + "..." # Сокращаем адрес для удобства чтения
            w_balance = balances_list[w_index] # Определяем баланс
            activity = random.choice(activities_list) # Выбираем случайную активность
            cex_funding = round(random.uniform(1, 3), 2) # Определяем сумму вывода с биржи для пополнения адреса
            activity_cost = round(random.uniform(1, 2), 2) # Определяем стоимость активности

            if w_balance == 0: # Если баланс == 0, поплняем баланс
                print(f'Funding wallet {wallet_short} from CEX for {cex_funding}')
                w_balance += cex_funding # Прибавляем сумму вывода с биржи к сумме баланса
                print(f'Wallet {wallet_short} balance: {w_balance:.2f} after funding from CEX for: {cex_funding}')
            else:
                print(f'Wallet {wallet_short} has balance > 0')

            if w_balance < activity_cost: # Если баланс меньше стоимости активности, пополняем адрес
                print(f'Starting {activity} for {activity_cost:.2f}...')
                print(f'Refuelling wallet {wallet_short} for {activity_cost - w_balance:.2f}')
                w_balance += activity_cost - w_balance # Пополнение баланса по формуле: баланс += стоимость активности-баланс
                print(f'Wallet {wallet_short} balance: {w_balance:.2f} after refuel')

            print(f'Wallet {wallet_short} is performing {activity}')
            w_balance -= activity_cost # Отнимаем от баланса стоимость активности
            print(f'Wallet {wallet_short} balance: {w_balance:.2f} after {activity}')
            tx_count_list[w_index] += 1 # Увеличиваем общее количество для адреса тх на 1
            wallet_activity_log[wallet][activity] += 1 # Увеличиваем общее количество тх для активности на выбранном адресе на 1
            balances_list[w_index] = w_balance # Обновляем значение баланса
            total_tx_count += 1 # Увеличиваем общее количество тх на 1
            print(f'Transaction {tx_count_list[w_index]} completed for wallet {wallet_short}')
            print("-" * 50) # Печатаем разделитель
            # time.sleep(1)  # Закомментировано для скорости выполнения

# Итоговые результаты:
for wallet, activities in wallet_activity_log.items(): # Для ключей, значений в элементах словаря-лога активностей по адресам
    print(f'Wallet {wallet}:') # Печатаем адрес
    for activity, count in activities.items(): # Для ключей, значений в элементах словаря активностей
        print(f'  {activity}: {count}') # Печатаем активность и количество

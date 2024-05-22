import random
import time

tx_target = int(input("Укажите желаемое число транзакций: "))

chars = "abcdef0123456789"

wallets_list = []

while len(wallets_list) < 10:
    address = "0x"
    while len(address) < 40:
        address += random.choice(chars)
    wallets_list.append(address)

tx_count_list = []

while len(tx_count_list) < len(wallets_list):
    tx_count_list.append(random.randint(0, 3))

completed_wallets = []

print("Запускаем работу...")
while any(tx_count < tx_target for tx_count in tx_count_list):
    chance = random.randint(0, 1)

    if chance:
        # Выбор случайного кошелька
        random_wallet = random.choice(wallets_list)
        wallet_index = wallets_list.index(random_wallet)
        tx_count = tx_count_list[wallet_index]
        if tx_count < tx_target:
            tx_increment = random.randint(1, 5)
            tx_count_list[wallet_index] += tx_increment
            print(
                f"Кошелек: {random_wallet} получил {tx_increment} транзакций, всего транзакций: {tx_count_list[wallet_index]}")
            if tx_count_list[wallet_index] >= tx_target:
                task = [random_wallet, tx_count_list[wallet_index]]
                completed_wallets.append(task)
                print(f"Кошелек {random_wallet} завершил выполнение задач.")
    else:
        # Выбор кошелька с минимальным количеством транзакций
        min_tx_count = min(tx_count_list)
        if min_tx_count < tx_target:
            wallet_index = tx_count_list.index(min_tx_count)
            min_wallet = wallets_list[tx_count_list.index(min_tx_count)]
            tx_increment = random.randint(1, 5)
            tx_count_list[wallet_index] += tx_increment
            print(
                f"Кошелек: {min_wallet} получил {tx_increment} транзакций, всего транзакций: {tx_count_list[wallet_index]}")
            if tx_count_list[wallet_index] >= tx_target:
                task = [min_wallet, tx_count_list[wallet_index]]
                completed_wallets.append(task)
                print(f"Кошелек {min_wallet} завершил выполнение задач.")

    time.sleep(random.uniform(0.1, 0.5))  # Пауза между транзакциями
print()
print("-"*50)
print("\nВсе кошельки выполнили минимальное количество транзакций.")
print("Список кошельков с завершенными задачами:")
i = 0
while i < len(completed_wallets):
    wallet, tx_count = completed_wallets[i]
    print(f"  Кошелек {wallet}: {tx_count}")
    i += 1

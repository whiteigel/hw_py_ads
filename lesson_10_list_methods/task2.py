import random
import time

activities = ['Swap', 'Bridge', 'Mint NFT', 'ENS registration', 'Liquidity provision',]
chars = "abcdef0123456789"

wallets_list = []

# Генерируем кошельки
while len(wallets_list) < 10:
    address = "0x"
    while len(address) < 42:
        address += random.choice(chars)
    wallets_list.append(address)

tasks_done = []

# Выполняем активности
while len(tasks_done) < len(wallets_list) * len(activities):
    wallet = random.choice(wallets_list)
    activity = random.choice(activities)
    task = [wallet, activity]
    if task not in tasks_done:
        tasks_done.append(task)
        print(f"Кошелек: {wallet}")
        print(f"    Выполняется активность: {activity}")
        time.sleep(0.5)
# print(tasks_done)
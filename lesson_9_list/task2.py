import time
import random

while True:
    wallets_num = input("Enter the number of wallets: ")
    if wallets_num.isdigit():
        wallets_num = int(wallets_num)
        break
    else:
        print("Invalid input")

while True:
    drop_num = input("Enter the number of drops: ")
    if drop_num.isdigit():
        drop_num = int(drop_num)
        break
    else:
        print("Invalid input")

print(wallets_num, drop_num)

wallets_count = 0
wallets_with_drop = []
target_gas = 30

while wallets_count < wallets_num:
    gas_price = 50
    wallets_count += 1
    if random.randint(0, 1) and drop_num > 0:
        print(f"Кошелек номер: {wallets_count} получил дроп")
        wallets_with_drop.append(wallets_count)
        drop_num -= 1
        while gas_price > target_gas:
            print(f"Газ выше {target_gas}. Ждем...")
            gas_price = random.randint(15, 50)
            time.sleep(1)
        print(f"Газ {gas_price}. Клеймим дроп!")
    else:
        print(f"Кошелек номер: {wallets_count} не получил дроп")

    if drop_num != 0 and wallets_count == wallets_num:
        wallets_count = 0

print(f"Кошельки с дропом: {wallets_with_drop}")
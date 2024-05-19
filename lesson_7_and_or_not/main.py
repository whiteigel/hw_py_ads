import random
import time

print("Task #1")
print()

input_digit = int(input("Enter a number: "))

if not input_digit:
    print("0 is zero")
else:
    parity = "even" if input_digit % 2 == 0 else "odd"
    negativity = "positive" if input_digit > 0 else "negative"
    print(f'{input_digit} is {parity} and {negativity}')

print("-"*50)
print()
print("Task #2")
print()

pwd_len = int(input("Enter a password length: "))
pwd_digit = input("Do you need digits in your password? (y/n): ")
pwd_string_letters = input("Do you need string letters in your password? (y/n): ")
pwd_cap_letters = input("Do you need capital letters in your password? (y/n): ")
pwd_special_char = input("Do you need special characters in your password? (y/n): ")

letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
special_characters = '!@#$%^&*'

password = []

# PWD length set
if 5 <= pwd_len <= 8:
    pwd_len = int(pwd_len)
else:
    pwd_len = random.randint(5, 8)

# PWD digits usage
if pwd_digit == "y":
    in_pwd_digits = random.choice(digits)
    password.append(in_pwd_digits)

# PWD string letters usage
if pwd_string_letters == "y":
    in_pwd_string_letters = random.choice(letters)
    password.append(in_pwd_string_letters)

# PWD capitals usage
if pwd_cap_letters == "y":
    in_pwd_cap_letters = random.choice(letters).upper()
    password.append(in_pwd_cap_letters)

# PWD special chars usage
if pwd_special_char == "y":
    in_pwd_special_char = random.choice(special_characters)
    password.append(in_pwd_special_char)

if pwd_digit != "y" and pwd_string_letters != "y" and pwd_cap_letters != "y" and pwd_special_char != "y":
    print("No characters selected, please try again")
else:
    while len(password) < pwd_len:
        if pwd_digit == "y" and len(password) < pwd_len:
            password.append(random.choice(digits))
        if pwd_string_letters == "y" and len(password) < pwd_len:
            password.append(random.choice(letters))
        if pwd_cap_letters == "y" and len(password) < pwd_len:
            password.append(random.choice(letters).upper())
        if pwd_special_char == "y" and len(password) < pwd_len:
            password.append(random.choice(special_characters))

    # Перемешивание символов в пароле
    random.shuffle(password)

    # Ограничение длины пароля до указанной
    final_password = ''.join(password[:pwd_len])
    print("Generated password:", final_password)

print("-"*50)
print()
print("Task #3")
print()

gas_price = round(random.uniform(15, 25), 2)
wallet_balance = round(random.uniform(0, 2), 4)
tx_count = random.randint(0, 3)

bridge_cost = 2
swap_cost = 1

if not tx_count:
    gas_price = round(random.uniform(15, 25), 2)
    print(f'Gas price: {gas_price}, wallet balance: {wallet_balance}, tx count: {tx_count}')
    time.sleep(1)

    if not wallet_balance:
        deposit = random.uniform(1, 2)
        wallet_balance += deposit
        print(f"Withdraw from CEX {round(deposit, 4)}")

    activity = "Bridge" if gas_price <= 20 else "Swap"
    print(f"Activity: {activity}")

    if activity == "Bridge":
        print("Bridging...")
        time.sleep(1)
        if wallet_balance < bridge_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(bridge_cost-wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += bridge_cost-wallet_balance
            print(f"Balance increased for {round(bridge_cost-wallet_balance, 4)}. "
                  f"Balance is now {round(wallet_balance, 4)}")
        wallet_balance -= bridge_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
    else:
        print("Swapping...")
        time.sleep(1)
        if wallet_balance < swap_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(swap_cost-wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += swap_cost-wallet_balance
            print(f"Balance increased for {round(swap_cost-wallet_balance, 4)}. "
                  f"Balance is now {wallet_balance}")
        wallet_balance -= swap_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
print()
if tx_count == 1:
    gas_price = round(random.uniform(15, 25), 2)
    print(f'Gas price: {gas_price}, wallet balance: {wallet_balance}, tx count: {tx_count}')
    time.sleep(1)

    if not wallet_balance:
        deposit = random.uniform(1, 2)
        wallet_balance += deposit
        print(f"Withdraw from CEX {round(deposit, 4)}")

    activity = "Bridge" if gas_price <= 20 else "Swap"
    print(f"Activity: {activity}")

    if activity == "Bridge":
        print("Bridging...")
        time.sleep(1)
        if wallet_balance < bridge_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(bridge_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += bridge_cost - wallet_balance
            print(
                f"Balance increased for {round(bridge_cost - wallet_balance, 4)}. "
                f"Balance is now {round(wallet_balance, 4)}")
        wallet_balance -= bridge_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
    else:
        print("Swapping...")
        time.sleep(1)
        if wallet_balance < swap_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(swap_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += swap_cost - wallet_balance
            print(f"Balance increased for {round(swap_cost - wallet_balance, 4)}. "
                  f"Balance is now {wallet_balance}")
        wallet_balance -= swap_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
print()
if tx_count == 2:
    gas_price = round(random.uniform(15, 25), 2)
    print(f'Gas price: {gas_price}, wallet balance: {wallet_balance}, tx count: {tx_count}')
    time.sleep(1)

    if not wallet_balance:
        deposit = random.uniform(1, 2)
        wallet_balance += deposit
        print(f"Withdraw from CEX {round(deposit, 4)}")

    activity = "Bridge" if gas_price <= 20 else "Swap"
    print(f"Activity: {activity}")

    if activity == "Bridge":
        print("Bridging...")
        time.sleep(1)
        if wallet_balance < bridge_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(bridge_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += bridge_cost - wallet_balance
            print(
                f"Balance increased for {round(bridge_cost - wallet_balance, 4)}. "
                f"Balance is now {round(wallet_balance, 4)}")
        wallet_balance -= bridge_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
    else:
        print("Swapping...")
        time.sleep(1)
        if wallet_balance < swap_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(swap_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += swap_cost - wallet_balance
            print(f"Balance increased for {round(swap_cost - wallet_balance, 4)}. "
                  f"Balance is now {wallet_balance}")
        wallet_balance -= swap_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
print()
if tx_count == 3:
    gas_price = round(random.uniform(15, 25), 2)
    print(f'Gas price: {gas_price}, wallet balance: {wallet_balance}, tx count: {tx_count}')
    time.sleep(1)

    if not wallet_balance:
        deposit = random.uniform(1, 2)
        wallet_balance += deposit
        print(f"Withdraw from CEX {round(deposit, 4)}")

    activity = "Bridge" if gas_price <= 20 else "Swap"
    print(f"Activity: {activity}")

    if activity == "Bridge":
        print("Bridging...")
        time.sleep(1)
        if wallet_balance < bridge_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(bridge_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += bridge_cost - wallet_balance
            print(
                f"Balance increased for {round(bridge_cost - wallet_balance, 4)}. "
                f"Balance is now {round(wallet_balance, 4)}")
        wallet_balance -= bridge_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
    else:
        print("Swapping...")
        time.sleep(1)
        if wallet_balance < swap_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(swap_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += swap_cost - wallet_balance
            print(f"Balance increased for {round(swap_cost - wallet_balance, 4)}. "
                  f"Balance is now {wallet_balance}")
        wallet_balance -= swap_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
print()
if tx_count == 4:
    gas_price = round(random.uniform(15, 25), 2)
    print(f'Gas price: {gas_price}, wallet balance: {wallet_balance}, tx count: {tx_count}')
    time.sleep(1)

    if not wallet_balance:
        deposit = random.uniform(1, 2)
        wallet_balance += deposit
        print(f"Withdraw from CEX {round(deposit, 4)}")

    activity = "Bridge" if gas_price <= 20 else "Swap"
    print(f"Activity: {activity}")

    if activity == "Bridge":
        print("Bridging...")
        time.sleep(1)
        if wallet_balance < bridge_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(bridge_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += bridge_cost - wallet_balance
            print(
                f"Balance increased for {round(bridge_cost - wallet_balance, 4)}. "
                f"Balance is now {round(wallet_balance, 4)}")
        wallet_balance -= bridge_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
    else:
        print("Swapping...")
        time.sleep(1)
        if wallet_balance < swap_cost:
            print(f"Not enough balance for {activity}. Withdraw from CEX {round(swap_cost - wallet_balance, 4)}")
            time.sleep(1)
            wallet_balance += swap_cost - wallet_balance
            print(f"Balance increased for {round(swap_cost - wallet_balance, 4)}. "
                  f"Balance is now {wallet_balance}")
        wallet_balance -= swap_cost
        tx_count += 1
        print(f"Wallet balance: {round(wallet_balance, 4)}, tx count: {tx_count}")
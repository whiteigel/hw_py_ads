import string
import time
import random
from typing import List

wallets_list = []


def wallet_list_generator(wallet_number: int) -> List[str]:
    global wallets_list
    wallets_list = ["0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40))
                    for _ in range(wallet_number)]
    return wallets_list


def password_generator(length: int, letters: bool, digits: bool, chars: bool) -> str:
    if not (letters or digits or chars):
        print("Укажите хотя бы один тип символов")
        return ""

    used_chars = ""
    if letters:
        used_chars += string.ascii_letters
    if digits:
        used_chars += string.digits
    if chars:
        used_chars += string.punctuation

    password = ''.join(random.choice(used_chars) for _ in range(length))
    return password


def gas_checker(gas_limit: int) -> int:
    while True:
        gas_price = random.randint(10, 50)
        if gas_price >= gas_limit:
            print(f'Газ высокий. Газ: {gas_price}')
            time.sleep(0.1)
        else:
            print(f'Можно работать. Газ: {gas_price}')
            return gas_price


def withdraw_from_cex(address: str, min_balance: float) -> float:
    print(f"Проверяем баланс адреса {address}...")
    time.sleep(1)
    balance = random.uniform(700, 1200)
    if balance < min_balance:
        min_to_amount = (min_balance - balance) * random.uniform(1.11, 1.23)
        balance += min_to_amount
        print(f"Сумма к выводу: {min_to_amount:.2f}")
        time.sleep(1)
    return balance


def main(wallet_num: int):
    wallet_list_generator(wallet_num)

    for wallet in wallets_list:
        password = password_generator(length=12, letters=True, digits=True, chars=True)
        print(f'Адрес: {wallet}, пароль: {password}')
        gas_checker(gas_limit=30)
        balance = withdraw_from_cex(address=wallet, min_balance=1000)
        print(f'Адрес: {wallet}, баланс: {balance:.2f}')
        print("-" * 50)
        time.sleep(1)


if __name__ == '__main__':
    main(wallet_num=5)

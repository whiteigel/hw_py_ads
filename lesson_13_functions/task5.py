import string
import time
import random
from typing import List

wallets_list = []


def wallet_list_generator(wallet_number: int) -> List[str]:
    """
    This function generates a list of all wallets in the system.
    :param wallet_number: Number of required wallets
    :return: a list of wallets in the system.
    """
    global wallets_list
    wallets_list = ["0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40))
                    for _ in range(wallet_number)]
    return wallets_list


def password_generator(length: int, letters: bool, digits: bool, chars: bool) -> str:
    """
    This function generates a random password.
    :param length: length of the password.
    :param letters: True if the password should be a letter.
    :param digits:  True if the password should be a digit.
    :param chars:  True if the password should be a character.
    :return: a random password.
    """
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
    """
    This function checks the gas limit.
    :param gas_limit: Working gas limit
    :return: current gas if higher than limit, else working gas
    """
    while True:
        gas_price = random.randint(10, 50)
        if gas_price >= gas_limit:
            print(f'Газ высокий. Газ: {gas_price}')
            time.sleep(0.1)
        else:
            print(f'Можно работать. Газ: {gas_price}')
            return gas_price


def withdraw_from_cex(address: str, min_balance: float) -> float:
    """
    This function imitates the withdrawal function.
    :param address: address of the wallet.
    :param min_balance: minimum balance of the wallet.
    :return: refilled balance of the wallet.
    """
    print(f"Проверяем баланс адреса {address}...")
    time.sleep(1)
    balance = random.uniform(700, 1200)
    if balance < min_balance:
        min_to_amount = (min_balance - balance) * random.uniform(1.11, 1.23)
        balance += min_to_amount
        print(f"Сумма к выводу: {min_to_amount:.2f}")
        time.sleep(1)
    return balance


def build_dict(dictionary: dict, wallet: str, password: str, balance: float) -> dict:
    """
    This function builds a working dictionary.
    :param dictionary: working dictionary.
    :param wallet: wallet address.
    :param password: account password.
    :param balance: balance of the wallet.
    :return: dictionary - Functioned{wallet:{password:password, balance:balance}
    """
    item_dict = {'password': password, 'balance': round(balance, 2)}
    dictionary[wallet] = item_dict
    return dictionary


def print_stats(dictionary: dict):
    """
    This function prints statistics.
    :param dictionary: working dictionary.
    :return: Strings of wallet statistics
    """
    print("\nСтатистика:\n")
    for wallet in dictionary.keys():
        print(f'Адрес: {wallet}')
        for key, value in dictionary[wallet].items():
            if key == 'password':
                key = 'пароль'
            else:
                key = 'баланс'
            print(f'---{key}: {value}')
        print("-" * 50)


def main(wallet_num: int):
    wallets_dict = {}
    wallet_list_generator(wallet_num)

    for wallet in wallets_list:
        password = password_generator(length=12, letters=True, digits=True, chars=True)
        print(f'Адрес: {wallet}, пароль: {password}')
        gas_checker(gas_limit=30)
        balance = withdraw_from_cex(address=wallet, min_balance=1000)
        print(f'Адрес: {wallet}, баланс: {balance:.2f}')
        build_dict(dictionary=wallets_dict, wallet=wallet, password=password, balance=balance)
        print("-" * 50)
        time.sleep(1)
    print_stats(dictionary=wallets_dict)


if __name__ == '__main__':
    main(wallet_num=5)

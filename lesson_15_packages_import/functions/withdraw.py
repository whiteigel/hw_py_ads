import time
import random


def check_balance(currency: str, address: str, chain: str) -> float:
    """
    Function checks account balance and returns balance
    :param currency: string with currency code
    :param address: string with account address
    :param chain: string with currency chain
    :return: float with balance
    """
    print(f'Checking balance for {currency} on {chain} for {address}')
    time.sleep(1)
    balance = random.uniform(0.01, 100)
    print(f'Balance: {balance} {currency} on {chain} for {address}')
    return balance


def withdraw_binance(amount: float, currency: str, address: str, chain: str) -> float:
    """
    Functions performs finding from Binance and returns balance
    :param amount: float amount to withdraw
    :param currency: string with currency code
    :param address:
    :param chain:
    :return: float with balance
    """
    balance = check_balance(currency, address, chain)
    print(f'Withdrawing from Binance {amount} {currency} to {address} on {chain}')
    time.sleep(1)
    print(f'Balance after funding: {balance + amount}')
    return balance + amount


def withdraw_okx(amount: float, currency: str, address: str, chain: str) -> float:
    """
    Functions performs finding from OKX and returns balance
    :param amount: float amount to withdraw
    :param currency: string with currency code
    :param address:
    :param chain:
    :return: float with balance
    """
    balance = check_balance(currency, address, chain)
    print(f'Withdrawing from OKX {amount} {currency} to {address} on {chain}')
    time.sleep(1)
    print(f'Balance after funding: {balance+amount}')
    return balance+amount


def withdraw_bybit(amount: float, currency: str, address: str, chain: str) -> float:
    """
    Functions performs finding from Bybit and returns balance
    :param amount: float amount to withdraw
    :param currency: string with currency code
    :param address:
    :param chain:
    :return: float with balance
    """
    balance = check_balance(currency, address, chain)
    print(f'Withdrawing from Bybit {amount} {currency} to {address} on {chain}')
    time.sleep(1)
    print(f'Balance after funding: {balance+amount}')
    return balance+amount

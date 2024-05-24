import random
import time


def withdraw_from_cex(address: str, min_balance: float) -> float:
    print("Проверяем баланс...")
    time.sleep(1)
    balance = random.uniform(0.01, 0.15)
    print(balance)
    if balance < min_balance:
        min_to_amount = (min_balance - balance) * random.uniform(1.11, 1.23)
        balance += min_to_amount
        print(f"Сумма к выводу: {min_to_amount}")
        time.sleep(1)
        print(f"Баланс: {balance}")
    return balance


withdraw_from_cex("23423432", 0.1)
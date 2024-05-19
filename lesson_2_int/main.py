import random

print('Task #1')
print()
num_1 = 5
num_2 = 15
withdraw_amount = random.randint(num_1, num_2)
print(f'Выводим на кошелек сумму равную {withdraw_amount}')
print()
print('-----'*10)
print()
print('Task #2')
print()
number = -15
print(abs(number) + 10)
print()
print('-----'*10)
print()
print('Task #3')
print()
num_input = int(input('Введите число: '))
if num_input % 2 == 0:
    print(True)
else:
    print(False)
print()
print('-----' * 10)
print()
print('Task #4')
print()

# Характеристики кошелька
wallet_balance = 0.01
tx_cont = 10
tx_amount = 5000
avg_tx_amount = tx_amount / tx_cont

# Минимальные критерии дропа
min_drop_tx_amount = 200
min_drop_tx_count = 10
drop_avg_tx_amount = 20
min_drop_balance = 0.005

# Проверка - вариант 1
eligible = all([
    wallet_balance >= min_drop_balance,
    tx_cont >= min_drop_tx_count,
    tx_amount >= min_drop_tx_amount,
    avg_tx_amount >= drop_avg_tx_amount
])

print(eligible)

# Проверка - вариант 2
if wallet_balance >= min_drop_balance and tx_cont >= min_drop_tx_count and avg_tx_amount >= drop_avg_tx_amount and tx_amount >= min_drop_tx_amount:
    print(True)
else:
    print(False)
print()
print('-----' * 10)
print()
print("Task4: class version")
print()


class DropCheck:
    min_drop_tx_amount = 200
    min_drop_tx_count = 10
    drop_avg_tx_amount = 20
    min_drop_balance = 0.005

    def __init__(self, wallet_balance: float, tx_cont: int, tx_amount: int):
        self.wallet_balance = wallet_balance
        self.tx_cont = tx_cont
        self.tx_amount = tx_amount
        self.avg_tx_amount = self.get_avg_tx_amount()
        self.eligible = self.is_eligible()

    def get_avg_tx_amount(self):
        return self.tx_amount / self.tx_cont

    def is_eligible(self):
        return all([
            self.wallet_balance >= DropCheck.min_drop_balance,
            self.tx_cont >= DropCheck.min_drop_tx_count,
            self.tx_amount >= DropCheck.min_drop_tx_amount,
            self.avg_tx_amount >= DropCheck.drop_avg_tx_amount
        ])

    def __str__(self):
        return f'{self.is_eligible()}'


sybil = DropCheck(wallet_balance=0.01, tx_cont=10, tx_amount=5000)
print(sybil)
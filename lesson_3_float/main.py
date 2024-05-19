import random

print("Task 1")
print()

float_num = 2.345554342

print(f'Ваше число: {float_num:.4f}')
print()

print("-----"*10)
print("Task 2")
print()

with_amount_min = 0.001
with_amount_max = 0.09

#  Вариант 1
print(f"Ваша сумма вывода: {round(random.uniform(with_amount_min, with_amount_max), 4)} ETH")

#  Вариант 2
print(f"Ваша сумма вывода: {random.uniform(with_amount_min, with_amount_max):.4f} ETH")
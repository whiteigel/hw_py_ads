import random

random_gas = random.randint(1, 100)
countdown = 60
gas_list = []

while countdown > 0:
    chance = random.randint(0, 1)
    random_gas += 1 if chance == 1 else -1
    countdown -= 1
    gas_list.append(random_gas)
print("Список значений газа за минуту: ", gas_list)
print("Среднее значение газа за минуту: ", round((sum(gas_list) / len(gas_list)), 2))

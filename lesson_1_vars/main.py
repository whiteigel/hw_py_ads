import time
# Task #1

print("Task #1")
print()
class Sybil:
    def __init__(self, name: str, acc_count: int, drop_value: int, lambo_cost: int):
        self.name = name
        self.acc_count = acc_count
        self.drop_value = drop_value
        self.drop_total = self.drop_value * self.acc_count
        self.lambo_cost = lambo_cost
        self.lambo_count = self.drop_total // self.lambo_cost

    def __str__(self):
        message = f'Hello, Brayan! My name is {self.name}, I have {self.acc_count} accs LayerZero'
        return message

    def wanna_drop(self):
        message = f'I want airdrop {self.drop_value}$ for every acc'
        return message

    def give_me_drop(self):
        message = f'Give me my drop: {self.drop_value}$ * {self.acc_count} accs = {self.drop_total}$'
        return message

    def wanna_labo(self):
        message = f'I want to buy Lambo, Lambo price is {self.lambo_cost}$'
        return message

    def wanna_more_lambos(self):
        message = f'I want to buy {self.lambo_count} Lambo'
        return message


sybil_max = Sybil(name='Max', acc_count=1000, drop_value=1000, lambo_cost=300000)

print(sybil_max)
print(sybil_max.wanna_drop())
print(sybil_max.give_me_drop())
print(sybil_max.wanna_labo())
print(sybil_max.wanna_more_lambos())
print()
print("-----"*10)

# Task #2
print("Task #2")
print()
surname = "Max"
name = "Zarev"
name, surname = surname, name
full_name = name + " " + surname
print(f"My name is {name}, my surname is {surname}")
print(f"My full name is {full_name}")
print()
print("-----"*10)
print()

# Task #3
print("Task #3")
print()
total = 0

for i in range(4):
    total += 10
    print(total)
print()
print("-----" * 10)
print()

# Task #4
print("Task #4")
print()
def make_shawarma(ingredient: str, lavash: str):
    print(f'Привет! Начинаю готовить ваш заказ')
    time.sleep(2)
    print(f'Беру {lavash}...')
    time.sleep(2)
    print(f'Готовлю начинку с {ingredient}...')
    time.sleep(2)
    print(f'Заворачиваю {ingredient} в {lavash}...')
    time.sleep(2)
    print(f'Еще немного...')
    time.sleep(2)
    print(f'А хотите расскажу анекдот, пока ваша шаурма из {ingredient} в {lavash} готовится?')
    time.sleep(2)
    print("Шаверма - это такая еда, которая может превратить обычный день в праздник просто одним грызом!")
    time.sleep(2)
    print(f'Пожалуйста! Ваша шаурма из {ingredient} с {lavash} готова! Приятного аппетита!')


make_shawarma(ingredient="овощи", lavash="лаваш с сыром")
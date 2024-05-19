import random

print("Task #1")
print()


def make_debank_url(address):
    return "https://debank.com/profile/"+address


url = "0xac8ce8fbc80115a22a9a69e42f50713aae9ef2f7"
print(make_debank_url(url))

print()
print("-----"*10)
print()

print("Task #2")
print()

letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%^&*'

# List variant
# password = [
#     random.choice(letters),
#     random.choice(letters.upper()),
#     random.choice(digits),
#     random.choice(special_characters)
# ]

# Tuple variant
# password = (
#     random.choice(letters),
#     random.choice(letters.upper()),
#     random.choice(digits),
#     random.choice(special_characters)
# )

# String variant 1
# password = (
#     random.choice(letters) +
#     random.choice(letters.upper()) +
#     random.choice(digits) +
#     random.choice(special_characters)
# )

# String variant 2
password = f"{random.choice(letters)}{random.choice(letters.upper())}{random.choice(digits)}{random.choice(special_characters)}"

print("Сгенерированный пароль:", ''.join(random.sample(password, len(password))))

print()
print("-----"*10)
print()

print("Task #3")
print()


def check_password_len(password):
    if len(password) < 8:
        return False
    else:
        return True


print(check_password_len("1234567453"))

print()
print("-----"*10)
print()

print("Task #4")
print()

data_string = input("Введите имя, фамилию и возраст: ")
name, surname, age = data_string.strip().split(" ")
print((name+" ")*3, (surname+ " ")*4, int(age)+10)

print()
print("-----"*10)
print()

print("Task #5")
print()

# Variant 1
def draw_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars + spaces)
    print(" " * (height - 1) + "*")
    print(" " * (height - 2) + "***")


draw_tree(6)
print()

# Variant 2
# print(f'{(" "*5)}*')
# print(f'{(" "*4)}{'*'*3}')
# print(f'{(" "*3)}{'*'*5}')
# print(f'{(" "*2)}{'*'*7}')
# print(f'{(" "*1)}{'*'*9}')
# print(f'{'*'*11}')
# print(f'{(" "*5)}*')
# print(f'{(" "*4)}{'*'*3}')

print()
print("-----"*10)
print()

print("Task #6")
print()

print("Текст в обратном порядке:", input("Введите текст: ")[::-1])

print()
print("-----"*10)
print()

print("Task #6")
print()

PASSWORD = "Password0"


def password_check(password):
    if password == PASSWORD:
        return True
    else:
        return False


print(password_check("Password0"))

print()
print("-----"*10)
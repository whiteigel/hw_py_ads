import random

# Ввод данных от пользователя
pwd_count = int(input("Введите требуемое количество паролей: "))
pwd_len = int(input("Введите длину пароля: "))
pwd_digit = input("Нужны ли цифры в пароле? (y/n): ")
pwd_string_letters = input("Нужны ли строчные буквы в пароле? (y/n): ")
pwd_cap_letters = input("Нужны ли заглавные буквы в пароле? (y/n): ")
pwd_special_char = input("Нужны ли специальные символы в пароле? (y/n): ")

letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
special_characters = '!@#$%^&*'

password_list = []

# Проверка длины пароля
if not (5 <= pwd_len <= 8):
    pwd_len = random.randint(5, 8)

# Генерация паролей
passwords_generated = 0
while passwords_generated < pwd_count:
    password = []

    # Добавление обязательных символов
    if pwd_digit == "y":
        password.append(random.choice(digits))
    if pwd_string_letters == "y":
        password.append(random.choice(letters))
    if pwd_cap_letters == "y":
        password.append(random.choice(letters).upper())
    if pwd_special_char == "y":
        password.append(random.choice(special_characters))

    # Проверка наличия выбранных типов символов
    if not password:
        print("Не выбрано ни одного типа символов, попробуйте снова")
        break

    # Заполнение остальной части пароля
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
    password_list.append(final_password)
    passwords_generated += 1

# Вывод списка сгенерированных паролей
print("Сгенерированные пароли:", password_list)
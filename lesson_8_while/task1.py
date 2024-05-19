import random

while True:
    secret_num = random.randint(1, 50)
    tries = 5
    counter = 0
    # print(secret_num)
    print('Привет! Давай сыграем в "Угадайку". Я загадал число от 1 до 50. Попробуй отгадать его.')

    while counter < tries:
        user_input = input("Введи число от 1 до 50: ")
        if not user_input.isdigit():
            print("Это не число. Введи число от 1 до 50.")
            continue

        counter += 1
        guess = int(user_input)

        if guess == secret_num:
            print(f"Ты отлично справился! Тебе потребовалось всего {counter} попыток!")
            break
        else:
            if guess > secret_num:
                print(f"Мое число меньше. Использовано попыток: {counter}.")
            else:
                print(f"Мое число больше. Использовано попыток: {counter}.")

        if guess != secret_num and counter == tries:
            print("Какая досада! Ты проиграл :(.")

    revenge = input("Хочешь сыграть еще раз? (y/n): ").lower()
    if revenge != "y":
        print("Спасибо за игру!")
        break
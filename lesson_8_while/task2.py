import time

while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Invalid input")
    else:
        countdown_digit = int(user_input)
        if countdown_digit == 0:
            exit()
        while countdown_digit > 0:
            print(countdown_digit)
            countdown_digit -= 1
            time.sleep(0.5)
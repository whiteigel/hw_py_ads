import random
import string


def password_generator(length: int, letters: bool, digits: bool, chars: bool) -> str:
    if not (letters or digits or chars):
        print("Укажите хотя бы один тип символов")
        return ""

    used_chars = ""
    if letters:
        used_chars += string.ascii_letters
    if digits:
        used_chars += string.digits
    if chars:
        used_chars += string.punctuation

    password = ''.join(random.choice(used_chars) for _ in range(length))
    return password


generated_password = password_generator(length=30, letters=True, digits=True, chars=True)
print(generated_password)

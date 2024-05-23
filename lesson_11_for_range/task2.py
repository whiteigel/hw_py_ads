import random

pasword_list_new = ["".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8)) for _ in range(100)]
print(pasword_list_new)

password_uppers = [password.upper() for password in pasword_list_new]
print(password_uppers)

d_passwords = [password for password in password_uppers if "D" in password]
print(d_passwords)


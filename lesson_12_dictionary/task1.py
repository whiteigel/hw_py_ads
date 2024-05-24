import random

wallets_num = int(input("Укажите сколько кошельков нужно создать: "))
wallets_list = ["0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40)) for _ in range(wallets_num)]
balance_list = [random.randint(1, 1000) for _ in range(wallets_num)]
accounts_dict = {wallet:balance_list[ind] for ind, wallet in enumerate(wallets_list)}
print(accounts_dict)
for key, value in accounts_dict.items():
    if value % 2 == 0:
        accounts_dict[key] = value * 2
print(accounts_dict)


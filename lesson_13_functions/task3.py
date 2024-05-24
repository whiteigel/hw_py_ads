import random
from typing import List

wallets_list = []


def wallet_list_generator(wallet_number: int) -> List[str]:
    global wallets_list
    outer_wallets_list = ["0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40)) for _ in range(wallet_number)]
    return outer_wallets_list


wallet_list_generator(wallet_number=5)
print("Global var list: ", wallets_list)

import random
from typing import List

outer_wallets_list = []


def wallet_list_generator(wallet_number: int) -> List[str]:
    global outer_wallets_list
    inner_wallets_list = ["0x" + ''.join(random.choice("abcdef0123456789") for _ in range(40)) for _ in range(wallet_number)]
    outer_wallets_list = inner_wallets_list
    return outer_wallets_list


print(wallet_list_generator(wallet_number=5))
print("Global var list: ", outer_wallets_list)

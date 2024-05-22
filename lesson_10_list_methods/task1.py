import random
import time

wallet_num = int(input("Укажите, сколько кошельков нужно создать: "))
drop_num = int(input("Укажите, сколько дропов нужно раздать: "))

chars = "abcdef0123456789"

wallets_list = []

while len(wallets_list) < wallet_num:
    address = "0x"
    while len(address) < 40:
        address += random.choice(chars)
    wallets_list.append(address)
print("Список кошельков создан")
print(f"Количество дропов для раздачи: {drop_num}")

eligible_wallets = []

while len(eligible_wallets) < drop_num:
    if len(eligible_wallets) >= len(wallets_list):
        print("Все кошельки уже получили дроп")
        break

    random_wallet = random.choice(wallets_list)
    if random_wallet not in eligible_wallets:
        eligible_wallets.append(random_wallet)
        print(f"Кошелек {random_wallet} добавлен в список eligible кошельков")
        time.sleep(0.5)
    else:
        print(f"Кошелек {random_wallet} уже получил дроп и не может претендовать еще на один")
        time.sleep(0.5)

claimed_wallets = []

while len(eligible_wallets) != 0:
    wallet_to_claim = random.choice(eligible_wallets)
    claimed_wallets.append(wallet_to_claim)
    eligible_wallets.remove(wallet_to_claim)
    print(f"Кошелек {wallet_to_claim} заклеймил дроп")
    time.sleep(random.uniform(1, 3))

sub_accounts_list = []

while len(sub_accounts_list) < len(claimed_wallets):
    sub_account = "0x"
    while len(sub_account) < 40:
        sub_account += random.choice(chars)
    sub_accounts_list.append(sub_account)

#  Тут я заебался и сделал быстро и просто, сорри!

wallets_pairs = zip(claimed_wallets, sub_accounts_list)
for pair in wallets_pairs:
    print(f"Переводим средства с аккаунта {pair[0]} на суб-аккаунт {pair[1]}")
    time.sleep(random.uniform(1, 3))
print("All done!")

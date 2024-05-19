import random
import time

print("Task #1")
print()
def check_balance(balance: int) -> None:
    if not balance:
        print("Beggar")
    elif balance <= 100:
        print("Normis")
    elif 101 <= balance <= 1000:
        print("Degen")
    elif 1001 <= balance <= 10000:
        print("Whale")
    else:
        print("Elon Mask")


check_balance(balance=0)

print("-----"*10)
print()
print("Task #2")
print()

# Случайные значения для цены газа и баланса кошелька
gas_price = random.randint(10, 60)
wallet_balance = random.randint(2000, 10000)

# Константы для расчета стоимости операций
SCROLL_BRIDGE = gas_price * 25
SCROLL_INNER_SWAP = gas_price * 40
CLUSTERS_DOMAIN_MINT = gas_price * 100

# Значения цены газа и баланса кошелька, а также стоимость операций
print("Gas price:", gas_price)
print("Wallet balance:", wallet_balance)
print("SCROLL_BRIDGE:", SCROLL_BRIDGE)
print('SCROLL_INNER_SWAP:', SCROLL_INNER_SWAP)
print('CLUSTERS_DOMAIN_MINT:', CLUSTERS_DOMAIN_MINT)

report = []


# Если баланс недостаточен, выводим дополнительные средства
def get_funding(wallet_balance):
    needed_funding = sum([SCROLL_BRIDGE, SCROLL_INNER_SWAP, CLUSTERS_DOMAIN_MINT]) - wallet_balance
    print(f"Not enough money. Wallet balance: {wallet_balance}. Funding {needed_funding} from CEX...")
    time.sleep(2)
    wallet_balance += needed_funding
    print("Wallet balance:", wallet_balance)
    report.append(f'Funded from CEX. Wallet balance increased for {needed_funding}. '
                  f'Balance before actions was {wallet_balance}')
    return wallet_balance


# Scroll Bridge
def make_scroll_bridge(wallet_balance):
    print(f"Starting Scroll Bridge...")
    wallet_balance -= SCROLL_BRIDGE
    time.sleep(2)
    print("Scroll bridge is done!")
    print("Wallet balance:", wallet_balance)
    report.append('Scroll bridge was done')
    return wallet_balance


# Clusters Domain Mint
def make_domain_mint(wallet_balance):
    print(f"Starting Clusters Domain Mint...")
    wallet_balance -= CLUSTERS_DOMAIN_MINT
    time.sleep(2)
    print("Clusters Domain Mint is done!")
    print("Wallet balance:", wallet_balance)
    report.append('Clusters Domain Mint was done')
    return wallet_balance


# Scroll Inner Swap
def make_swap(wallet_balance):
    print(f"Starting Scroll Inner Swap")
    wallet_balance -= SCROLL_INNER_SWAP
    time.sleep(2)
    print("Scroll Inner Swap is done")
    print("Wallet balance:", wallet_balance)
    report.append('Scroll Inner Swap was done')
    return wallet_balance


# High gas. Take rest
def take_rest(gas_price):
    print(f"Gas price is high {gas_price}. Take a break")
    report.append(f'Gas price was high. No action done')
    return gas_price


def print_report(report):
    print("Report:")
    for action in report:
        print("-", action, )
    print(f"- Wallet balance: {wallet_balance}")


def main(wallet_balance, gas_price):
    if gas_price > 50:
        _ = take_rest(gas_price)

        # Печатаем отчет
        print_report(report)
        return

    # Проверяем баланс
    if wallet_balance < sum([SCROLL_BRIDGE, SCROLL_INNER_SWAP, CLUSTERS_DOMAIN_MINT]):
        wallet_balance = get_funding(wallet_balance)  # Получаем дополнительное финансирование

    # Проверяем цену газа
    if gas_price < 25:
        wallet_balance = make_scroll_bridge(wallet_balance)
        if gas_price <= 15:
            wallet_balance = make_domain_mint(wallet_balance)
    elif gas_price >= 25:
        wallet_balance = make_swap(wallet_balance)

    # Печатаем отчет
    print_report(report)


main(wallet_balance, gas_price)

print("-----"*10)
print()
print("Task #3")
print()

# Глобальные переменные для балансов ETH и USDC
balance_eth = random.uniform(0.08, 0.1)
balance_usdc = random.randint(100, 200)


def swap():
    global balance_eth, balance_usdc

    eth_value = random.randint(3000, 3500)

    if balance_usdc > 0:
        eth_to_add = min(balance_usdc / eth_value, balance_usdc)  # Переводим только доступное количество USDC
        balance_eth += eth_to_add
        balance_usdc -= eth_to_add * eth_value  # Вычитаем соответствующую сумму из баланса USDC
        print(f"Swapped {round(eth_to_add * eth_value, 2)} USDC to {round(eth_to_add, 4)} ETH")
    else:
        eth_to_sell = balance_eth * 0.95
        usdc_to_add = eth_to_sell * eth_value
        balance_eth -= eth_to_sell
        balance_usdc += usdc_to_add
        print(f"Swapped {round(eth_to_sell, 5)} ETH to USDC")

    return (f'Balance ETH = {round(balance_eth, 4)} ETH, balance USDC = {round(balance_usdc, 2)} USDC, '
            f'current ETH value = {eth_value} USDC')


for i in range(5):
    print(swap())
    time.sleep(random.randint(2, 3))
import random
from functions.withdraw import (withdraw_binance as w_b, withdraw_okx as w_okx,
                                withdraw_bybit as w_bybit)

addresses = ['0x3008099304a30800D8a89D27305Fe06fD9ed3337',
             '0x46Dbf7722b484CBd29cEA22D9b305923792B256C',
             '0x92bCbd4f26545Ba0e76024cD7aAa42766ba76CAd',
             '0x64684BCca02E8c349337022E8dCeC7d012A24EC0',
             '0x053C7ba445183638d955Ac37C292A37bE5f59E06',
             ]

cex_list = [w_b, w_bybit, w_okx]


main_func_dict = {
    'address_list': addresses,
    'chain': 'Scroll',
    'currency': 'ETH'
    }


def main(**kwargs):
    for address in kwargs['address_list']:
        withdraw_chain = kwargs['chain']
        withdraw_amount = random.uniform(0.08, 0.13)
        cex = random.choice(cex_list)
        withdraw_dict = {
            'amount': round(withdraw_amount, 4),
            'currency': kwargs['currency'],
            'address': address,
            'chain': withdraw_chain
            }
        cex(**withdraw_dict)
        print("-" * 50)


if __name__ == '__main__':
    main(**main_func_dict)
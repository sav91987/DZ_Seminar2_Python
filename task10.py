import random
num_coins = int(input('Введите количество монет: '))
count_coin_avers=0
count_coin_revers=0
for i in range(num_coins):
    coin = random.randint(0,1)
    print(coin)
    if coin == 0: count_coin_avers+=1
    else: count_coin_revers+=1
if count_coin_avers>count_coin_revers:
    print(f'Нужно перевернуть {count_coin_revers} монеты')
else: print(f'Нужно перевернуть {count_coin_avers} монеты')
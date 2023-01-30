#from random import choice
#coin = choice(["head","tail"])

import random


coin = random.choice(["head","tail"])

num = random.randint(1,20)  #picks random num from 1 to 10

print(coin,num)

cards = ["jack","queen","king"]
random.shuffle(cards)

for card in cards:
    print(card)









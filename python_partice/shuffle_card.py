import random 

cards = ["Ace", "King", "Queen", "Jack", "Joker"]
cards_1 = ["Ace", "King", "Queen", "Jack", "Joker"]
n = 0

while True:
    n = n + 1
    random.shuffle(cards_1)
    P = (1/n)*100
    if cards == cards_1:
        print(f" the same number of times?  {n}")
        break
    else:
        continue

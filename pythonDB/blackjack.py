#### BLACKJACK IN PYTHON #####
### CREATED BY DANIEL ALEXANDER BERRONES 5/26/2019 #######

import random

cards = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven',
         'Six', 'Five', 'Four', 'Three', 'Two', 'One']

suit = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

print("\nThe dealer shows: ")
print(random.choice(cards) + " of " + random.choice(suit))

print("\nYou have: ")
print(random.choice(cards) + " of " + random.choice(suit) + " \nand " + "\n" + random.choice(cards) + " of " + random.choice(suit))

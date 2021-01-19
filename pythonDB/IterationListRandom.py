#####################################
### PROGRAM BY DANIEL A. BERRONES ###
####### CREATED ON 12/23/2018 #######
#####################################

import random
import time

i = 0

to_learn = ['tuples', 'lists', 'ints', 'floats', 'if then statements', 'booleans',
            'functions', 'arrays', 'modules', 'methods', 'while loops', 'for loops',
            'import', 'strings', 'elif statements', 'dictionaries', 'break',
            'continue','return', 'try', 'except', 'pass', 'with', 'operands', 'append',
            'import os','random module', 'time module']

def abc():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

def simple():
    for x in to_learn:
        print()
        print("-",x)
        time.sleep(.2)



def gen():
    for x in range(0,100):
        global i
        print()
        i=i +  1
        print("This is iteration #",i)
        print()
        a = random.choice(to_learn)
        print("I randomly picked:",a)
        print()
        print()
        length = len(a)
        print("The length of "+a+" is:",length,"characters.")
        print()
        print()
        print()
        print("***********************************")
        print("***********************************")
        print("***********************************")
        print("***********************************")
        time.sleep(3)
        abc()
        if i % 2==0:
            print("As a reminder...")
        else:
            continue
        time.sleep(2)
        abc()
        print("The list contains these elements:")
        simple()
        abc()



gen()
import random, time

i=0

while True:
    print("Think of a number between 1-10")
    print()
    number=int(input("What's your number? "))
    rand=random.randint(1,10)
    if number==rand:
        print("Correct!")
        print("It took you: {} times".format(i))
        break
    print("Hmmmm... lemme think...")
    time.sleep(.5)
    print("NOPE! THE # WAS",rand)
    i += 1
    print()
    print()


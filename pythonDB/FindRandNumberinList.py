import random,time

def blank():
    print('\n' * 20)


sum=0
number=random.randint(0,20000)
blank()
print("***************")
print("***************")
print("5 ENDS PROGRAM")
print("***************")
print("***************")
time.sleep(3)
print()
print()
print("game begins in....")
blank()
print()
time.sleep(3)
print("3")
blank()
time.sleep(1)
print("2")
blank()
time.sleep(1)
blank()
print("1. . . ")
time.sleep(2)


while True:
    if number==5:
        print()
        print()
        print(" 5  HAS BEEN FOUND!!")
        print()
        time.sleep(2)
        print()
        blank()
        print()
        print("**********")
        print("**********")
        print("CONGRATS!!!!")
        print("**********")
        print("**********")
        print()
        print()
        time.sleep(2)
        print()
        print("It took you... ")
        print()
        print()
        print()
        blank()
        time.sleep(3)
        print()
        print(sum,"tries!")
        print("__________")
        print("__________")
        print()
        print()
        time.sleep(1)
        blank()
        print("Program ends in . . .")
        print()
        time.sleep(3)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        break
    else:
        number = random.randint(1, 100000)
        sum = sum + 1
        print("NUMBER NOW EQUALS: ",number)
        print()

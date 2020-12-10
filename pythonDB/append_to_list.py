import random, time

list1 = []
list2 = []
i=1
for x in range(20):
    print(f"\nThis is iteration: {i}")
    i += 1
    num = random.randint(1,2)
    if num == 1:
        print("Your number was 1")
        list1.append(num)
    elif num == 2:
        print("Your number was 2")
        list2.append(num)

print(len(list1))
print(len(list2))
print(list1)
print(list2)

def fib(n):
        if n == 0:
            return 0
        elif n== 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

i = 0


for x in range(20):
    print(fib(i))
    i += 1
    print("End of {} iteration".format(i))
    print()


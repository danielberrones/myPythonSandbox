print("\nProgram determines if number is even or odd.")
input(">> Press enter to continue...")

while True:
	num = eval(input("\nEnter a number: "))
	if num % 2 == 0:
		print("The number " + str(num) + " is even")
	else:
		print("The number " + str(num) + " is odd")
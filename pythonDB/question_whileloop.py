
def main():
	while True:
		print("whats your name?")
		name = input(">  ")
		if name != 'Daniel':
			print(f"no! you are {name}, and I am looking for someone else!")
			continue
		print(f"Okay, {name}, its my pleasure you made it here.")
		print("Whats your fav sex position?")
		posy = input(">> ")
		if posy != 'doggy':
			print("you lose dude!")
			continue
		print("YOU WIN BRAH!")
		break




main()
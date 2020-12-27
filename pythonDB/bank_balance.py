class BankAccount:
	def __init__(self, initial_balance):
		self.balance = initial_balance
		
	def deposit(self, amount):
		self.balance += amount
		return self.balance
		
	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
		
	def get_balance(self):
		return self.balance

def main():
	account = BankAccount(0)
	print("STARTING BALANCE: ", account.get_balance())
	print("Adding 10 to balance: NEW BALANCE: ", account.deposit(10))
	print("NEW BALANCE: ", account.get_balance())
	print("Withdrawing 150", account.withdraw(150))
	print("NEW BALANCE: ", account.get_balance())

	
	
			
main()
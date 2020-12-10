class Bank:
	def __init__ (self, balance):
		self.balance = balance
	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
	def deposit(self, amount):
		self.balance += amount
		return self.balance
	def statement(self):
		return self.balance
def main():
	b = Bank(0)	
	print("Your current statement: ", b.statement())
	print("Your current statement: ", b.statement())
	b.withdraw(150)
	b.statement()
	print(b.statement())
	b.deposit(1000)
	print(b.statement())
	
main()


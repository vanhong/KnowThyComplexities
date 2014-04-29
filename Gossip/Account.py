class Account:
	def __init__(self, number, name):
		self.number = number
		self.name = name
		self.balance = 0

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError('must be positive')
		acct.balance += amount

	def withdraw(self, amount):
		if amount <= acct.balance:
			acct.balance -= amount
		else:
			raise RuntimeError('balance not enough')

acct = Account('123-456-789', 'Justin')

print(acct.number)
print(acct.name)
acct.deposit(100)
print(acct.balance)
acct.withdraw(50)
print(acct.balance)
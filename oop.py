import unittest
"""
NARRATIVE/REQUIREMENTS
	An account has two sides to it representing incoming and outgoing flows
		debit (dr)
		credit (cr)
	which of the two represent which flow depends on the type of account in consideration
		Assets (What one owns)
			cr when decreasing, dr when increasing
		Liabilites (What one owes)
			dr when decreasing, cr when increasing
		Expenses (What one spends)
			cr when decreasing, dr when increasing
		Income (What one earns)
			dr when decreasing, cr when increasing

"""

class Account(object):
	__balance = 0

	def __init__(self, name):
		self.name = name

	def get_balance(self):
		return self.__balance

	def set_balance(self, bal):
		self.__balance = bal

class Asset(Account):
	def debit(self, amt):
		self.set_balance(self.get_balance() + amt)

	def credit(self, amt):
		self.set_balance(self.get_balance() - amt)

class Liability(Account):
	def debit(self, amt):
		self.set_balance(self.get_balance() - amt)

	def credit(self, amt):
		self.set_balance(self.get_balance() + amt)


class AccountTest(unittest.TestCase):
	#The following test case is a demonstration of an OBJECT
	def test_account_instance_of_object(self):
		acc = Account('Honda')
		self.assertIsInstance(acc, object, msg='The object should be an instance of the `object` class')

	#The following test cases are a demonstration of INHERITANCE
	def test_asset_instance_of_account(self):
		acc = Asset('Honda')
		self.assertIsInstance(acc, Account, msg='The object should be an instance of the `Account` class')

	def test_liability_instance_of_account(self):
		acc = Liability('Honda')
		self.assertIsInstance(acc, Account, msg='The object should be an instance of the `Account` class')

	def test_asset_instance_of_liability(self):
		acc = Asset('Honda')
		self.assertNotIsInstance(acc, Liability, msg='The object should not be an instance of the `Liability` class')

	def test_asset_has_balance(self):
		acc = Asset('Honda')
		self.assertEqual(acc.get_balance(), 0, msg='The object should have a balance attribute inherited from Account')

	#The following test cases are a demonstration of ENCAPSULATION
	def test_balance_access(self):
		acc = Asset('Honda')
		with self.assertRaises(AttributeError):
			acc._balance

	#The following test cases are a demonstration of POLYMORPHISM
	def test_asset_debit(self):
		acc = Asset('Honda')
		acc.debit(600)
		self.assertEqual(acc.get_balance(), 600, msg='The object should have a positive balance attribute when debit with a balance on 0')

	def test_liability_debit(self):
		acc = Liability('Honda')
		acc.credit(600)
		acc.debit(600)
		self.assertEqual(acc.get_balance(), 0, msg='The object should have a 0 balance attribute when debited 600 with a balance on 600')

if __name__ == "__main__":
	unittest.main()




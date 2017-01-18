from unittest import TestCase, main
from oop import TransactionStore, Transaction, Account, Asset, Liability

class AccountTest(TestCase):
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

	#The following test cases are a demonstration of COMPOSITION
	#to do

if __name__ == "__main__":
	main()
import time

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
	A transaction in this case is a change in the state of an account. It needs to show: 
		when the change occured,
		what was changed,
			To know this a transaction will need to know the:
				type of account being changed,
				the name of the account 
		the extent of change
		the action taken on the account,
"""

class TransactionStore:
	_ALL = {}

	def __init__(self):
		pass

	def save(self, trans):
		self._ALL[trans.get_time()] = [trans.get_amt(), trans.get_acctype(), trans.get_transtype()]
		print "Saving Transaction for "+trans.get_acctype()+" at "+trans.get_time()

	def print_all(self):
		for key, value in self._ALL.iteritems():
			print key
			print value
			print "Time %s : %s | %s | %s" % (str(key), value[0], value[1], str(value[2]))

"""
	Both the Transaction and TransactionStore are use to demonstration COMPOSITION
	An account makes use of the Transaction object to commit changes
	The Transaction makes use of the TransactionStore to store the changed
	The TransactionStore makes use of the Transaction to access when it is required to store
"""
class Transaction(object):
	__when = None
	__acctype = None #what
	__transtype = None #what
	__amt = 0 #extent

	def __init__(self, amt, acctype, transtype):
		self.__when = time.ctime()
		self.__amt = amt
		self.__acctype = acctype
		self.__transtype = transtype
		print "Created Transaction for "+self.__acctype+" at "+self.__when

	def commit(self):
		TransactionStore().save(self)
		TransactionStore().print_all()
	
	def get_time(self):
		return self.__when

	def get_amt(self):
		return self.__amt

	def get_acctype(self):
		return self.__acctype

	def get_transtype(self):
		return self.__transtype

class Account(object):
	__balance = 0

	def __init__(self, name):
		self.name = name
		print "Account instance created."

	def get_balance(self):
		print "Current balance: %d queried" % self.__balance
		return self.__balance

	def set_balance(self, bal):
		self.__balance = bal
		print "Current balance set to %d" % bal

	def debit(self, amt):
		print "Parent debit for "+self.__class__.__name__+" account"
		Transaction(amt, self.__class__.__name__, 'debit').commit()

	def credit(self, amt):
		print "Parent credit "+self.__class__.__name__+" account"
		Transaction(amt, self.__class__.__name__, 'credit').commit()


class Asset(Account):
	def debit(self, amt):
		Account.debit(self, amt)
		prevbal = self.get_balance()
		bal = self.get_balance() + amt
		print "Asset account: %s Debited %d, Balance changed from %d to %d" % (self.name, amt, prevbal, bal)
		self.set_balance(bal)

	def credit(self, amt):
		Account.credit(self, amt)
		prevbal = self.get_balance()
		bal = self.get_balance() - amt
		print "Asset account: %s Credited %d, Balance changed from %d to %d" % (self.name, amt, prevbal, bal)
		self.set_balance(bal)

class Liability(Account):
	def debit(self, amt):
		Account.debit(self, amt)
		prevbal = self.get_balance()
		bal = self.get_balance() - amt
		print "Liability account: %s Debited %d, Balance changed from %d to %d" % (self.name, amt, prevbal, bal)
		self.set_balance(bal)

	def credit(self, amt):
		Account.credit(self, amt)
		prevbal = self.get_balance()
		bal = self.get_balance() + amt
		print "Liability account: %s Credited %d, Balance changed from %d to %d" % (self.name, amt, prevbal, bal)
		self.set_balance(bal)







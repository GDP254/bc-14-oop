from oop import TransactionStore, Transaction, Account, Asset, Liability

"""
	A company needs equipment but cannot afford it
	Said company receives necessary equipment from a niche financial services company
	This company grant their clients equipment they refurbish with its monetary value determined by an independent trusted third party
	A deal was struck for equipment valued at 100,000
	Running the code below should print the steps involved in this transaciton i.e.
		Debit assets 100000
		Credit Liability 100000
"""

equipment = Asset('server')
equipment.debit(100000)
nichefsc = Liability('nichefscllc')
nichefsc.credit(100000)


class TransferCentre():


	def __init__(self):
		self._windowList = []
		self._contracts = []

	@property
	def contracts(self):
		return self._contracts

	def addContract(self, contract):
		contract.contractID = len(self._contracts)
		self._contracts.append(contract)

	def printContracts(self):
		for contract in self._contracts:
			print(contract)


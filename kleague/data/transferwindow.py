

class TransferWindow():


	def __init__(self):
		print('transfer window init')
		self._windowID = None
		self._contracts = []

	@property
	def windowID(self):
		return self._windowID

	@windowID.setter
	def windowID(self, windowID):
		self._windowID = windowID

	@property
	def contracts(self):
		return self._contracts

	def addContract(self, contract):
		self._contracts.append(contract)

	def __str__(self):
		output = ''
		output += '{ID: ' + str(self.windowID) + '}'
		return output

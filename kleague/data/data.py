from kleague.data.transfercentre import TransferCentre

class Data():


	def __init__(self):
		self._transferCentre = TransferCentre()

	def setData(self):
		1+1

	def getData(self):
		1+1

	def addTransferWindow(self, transferWindow):
		self._transferCentre.addTransferWindow(transferWindow)

	def getTransferWindow(self):
		self._transferCentre.getTransferWindow()

	def addContract(self, contract):
		self._transferCentre.addContract(contract)

	def getContracts(self):
		return self._transferCentre.contracts
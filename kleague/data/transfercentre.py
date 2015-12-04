from kleague.data.transferwindow import TransferWindow

class TransferCentre():


	def __init__(self):
		self._windowList = []
		self._contracts = []


	def addTransferWindow(self, transferWindow):
		transferWindow.windowID = len(self._windowList)
		self._windowList.append(transferWindow)

	def getTransferWindow(self):
		for window in self._windowList:
			print(window)

	@property
	def contracts(self):
		return self._contracts

	def addContract(self, contract):
		contract.contractID = len(self._contracts)
		self._contracts.append(contract)

	def printContracts(self):
		for contract in self._contracts:
			print(contract)


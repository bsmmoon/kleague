from kleague.data.transfercentre import TransferCentre

class Data():


	def __init__(self):
		print('data init')
		self.transferCentre = TransferCentre()

	def getData(self):
		print('data getData')

	def setData(self):
		print('data setData')

	def addTransferWindow(self, transferWindow):
		print('data addTransferWindow')
		self.transferCentre.addTransferWindow(transferWindow)

	def getTransferWindow(self):
		print('data getTransferWindow')
		self.transferCentre.getTransferWindow()



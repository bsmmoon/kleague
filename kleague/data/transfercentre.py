from kleague.data.transferwindow import TransferWindow

class TransferCentre():


	def __init__(self):
		print('transfer centre init')
		self.windowList = []


	def addTransferWindow(self, transferWindow):
		print('transfer centre addTransferWindow')
		self.windowList.append(transferWindow)

	def getTransferWindow(self):
		print('transfer centre getTransferWindow')
		print('size: ' + str(len(self.windowList)))


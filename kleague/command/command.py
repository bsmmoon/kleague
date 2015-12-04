from kleague.data import Contract


class Command():


	def __init__(self):
		self.data = None

	def insertData(self, data):
		self.data = data

	# def execute(self):

	# def undo(self):


class AddTransferWindow(Command):


	def __init__(self, transferWindow):
		self.transferWindow = transferWindow

	def execute(self):
		self.data.addTransferWindow(self.transferWindow)


class AddContract(Command):


	def __init__(self, contract):
		self.contract = contract

	def execute(self):
		self.data.addContract(self.contract)


from kleague.data import Contract


class Command():


	def __init__(self):
		print('command init')

	def insertData(self, data):
		print('command insert data')
		self.data = data

	def execute(self):
		print('command execute')

	def undo(self):
		print('command undo')


class AddTransferWindow(Command):


	def __init__(self, transferWindow):
		print('AddTransferWindow init')
		self.transferWindow = transferWindow

	def execute(self):
		print('AddTransferWindow execute')
		self.data.addTransferWindow(self.transferWindow)

	def undo(self):
		print('AddTransferWindow undo')


class AddPendingContract(Command):


	def __init__(self, tokens):
		print('AddPendingContract init')
		self.contract = Contract()

	def execute(self):
		print('AddPendingContract execute')
		self.data.addPendingContract(self.contract)

	def undo(self):
		print('AddPendingContract undo')
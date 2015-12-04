

class Command():


	def __init__(self):
		print('command init')
		self.data = data

	def insertData(self, data):
		print('command insert data')
		self.data = data

	def execute(self):
		print('command execute')

	def undo(self):
		print('command undo')


class AddTransferCentre(Command):


	def __init__(self, transferCentre):
		print('AddTransferCentre init')
		self.transferCentre = transferCentre

	def execute(self):
		print('AddTransferCentre execute')
		self.data.addTransferCentre(self.transferCentre)

	def undo(self):
		print('AddTransferCentre undo')


class Command():


	def __init__(self, data):
		print('command init')
		self.data = data

	def execute(self):
		print('command execute')

	def undo(self):
		print('command undo')


class AddTransferCentre(Command):


	def __init__(self, data, transferCentre):
		print('addTransferCentre init')
		self.data = data

	def execute(self):
		print('addTransferCentre execute')
		self.data.addTransferCentre(self.transferCentre)

	def undo(self):
		print('addTransferCentre undo')